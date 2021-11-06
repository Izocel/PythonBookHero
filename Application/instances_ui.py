import os
from typing import Concatenate
from PyQt5 import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *

# Workspace Related #
from gestion_ui import *


# CLASSES DE DIALOGUES #######################################################


#### ECRAN_USAGER ##############################################
# Extension de la classe provenant du designer (ecranusager.ui)
# Proprietées connu sur ECRAN_USAGER
    # ?
    # ?
    # ?
#
class ECRAN_USAGER(QDialog):

    parent = {}

    def __init__(self):
        super(ECRAN_USAGER, self).__init__()
        ui_path =  os.path.dirname(os.path.abspath(__file__))
        ui_path += '\\Bibli_ui\\ecranusager.ui'
        loadUi(ui_path, self)

    def setup_logics(self, w_parent):
        global parent
        parent = w_parent

        self.deconnectionpushButton.clicked.connect(lambda:self.deconnection_usagers_btnaction())

    
    def deconnection_usagers_btnaction(self):
        global parent
        ecran_acceuil = parent.findChild(QDialog, 'EcranAcceuil')
        ecran_acceuil.app_disconnect()
        ecran_acceuil.setup_logics(parent)
        parent.setCurrentIndex(parent.currentIndex()-1)


#### ECRAN_ACCEUIL ##############################################
# Extension de la classe provenant du designer (ecranacceuil.ui)
# Proprietées connu sur ECRAN_ACCEUIL
    # connectionpushButton (btn)
    # motdepasse_lineEdit (input)
    # courriel_lineEdit (input)
#
class ECRAN_ACCEUIL(QDialog):

    parent = {}
    logged_in = False

    def __init__(self):
        super(ECRAN_ACCEUIL, self).__init__()
        ui_path =  os.path.dirname(os.path.abspath(__file__))
        ui_path += '\\Bibli_ui\\ecranacceuil.ui'
        loadUi(ui_path, self)

        global logged_in
        logged_in = False

    def setup_logics(self, w_parent):
        global logged_in
        global parent
        parent = w_parent

        self.label_mauvaise_infos.hide()
        self.connectionpushButton.clicked.connect(lambda:self.connection_usagers_btnaction())
        
    
    def app_disconnect(self):
        global logged_in
        if(logged_in):
            logged_in = not mysql_app_disconnection()
            
        return logged_in
        
    def app_connect(self):
        global logged_in

        bd_config = ECRAN_ACCEUIL.get_bd_credentials(self)

        if(mysql_app_connection(bd_config, True)):

            logged_in = True
            mysql_app_create_tables()
            mysql_app_insert_user()
            
        return logged_in

    def get_bd_credentials(self):

        conn_fields = {}
        conn_fields['host'] = 'localhost'
        conn_fields['port'] = '3306'
        conn_fields['user'] = 'root' #TODO: Faire un user juste pour cette BD
        conn_fields['password'] = getpass("Entrer le mot de passe mysql: \n ==> ")

        return conn_fields


    def get_usager_credentials(self):

        conn_fields = {}
        conn_fields['courriel'] = self.courriel_lineEdit.text()
        conn_fields['hashmotpasse'] = hash_sha2_data([self.motdepasse_lineEdit.text()])[0]

        return conn_fields

    def connection_usagers_btnaction(self):
        global logged_in

        if(not logged_in):
            logged_in = self.app_connect()

        if(logged_in):
            user_cred = self.get_usager_credentials()
            acces_usager_promu = verif_connection_usager(**user_cred)

            if(acces_usager_promu):
                self.label_mauvaise_infos.hide()
                self.connectionpushButton.disconnect()

                ######### CHANGER DE PAGE  ############
                parent.setCurrentIndex(parent.currentIndex()+1)

            else: # Ajouter un message à l'écran de mauvaise infos....
                self.app_disconnect()
                self.label_mauvaise_infos.show()
            
#### ECRAN_CHAPITRE ##############################################
# Extension de la classe provenant du designer (ecranchapitre.ui)
# Proprietées connu sur ECRAN_CHAPITRE
    # ?
    # ?
    # ?
#
class ECRAN_CHAPITRE(QDialog):

    def __init__(self):
        super(ECRAN_CHAPITRE, self).__init__()
        ui_path =  os.path.dirname(os.path.abspath(__file__))
        ui_path += '\\Bibli_ui\\selectionchapitres.ui'
        loadUi(ui_path, self)

    def setup_logics(self, w_parent):
        #self.field_selection_chapitre() <-- ## Migrer vers une autre appel ou changer son setup_logics() de place...
        #self.connectionbtn.clicked.connect(lambda:self.connect_actionbtn())
        pass

    def field_selection_chapitre(self):
        index = 0

        self.selection_chapitre_comboBox.addItem("")
        self.selection_chapitre_comboBox.setItemText(index, "Sélectionnez un chapitre")
        index +=1

        self.selection_chapitre_comboBox.addItem("")
        self.selection_chapitre_comboBox.setItemText(index, "Nous somme désolés, aucune données disponible")


        chapitres = lister_chapitre()
        if(len(chapitres) > 0):
            for champs in chapitres:
                self.selection_chapitre_comboBox.addItem("")
                self.selection_chapitre_comboBox.setItemText(index, "chapitre " + str(champs[2]))
                index +=1