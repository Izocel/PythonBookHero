import os
from typing import Concatenate
from PyQt5 import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *

# Workspace Related #
from gestion_ui import *


# CLASSES DE DIALOGUES #######################################################



 #### EXAMPLE ####
# Extension de la classe provenant du designer (mainwindow.ui)
# Proprietées connu sur LOGIN_W(mainwindow)
    # hostfield (input)
    # portfield (input)
    # userfield (input)
    # passwordfield (input)  pyCrudApp\ui_designs
    # connectionbtn (button)
#
class ECRAN_DEV(QDialog):

    def __init__(self):
        super(ECRAN_DEV, self).__init__()
        ui_path =  os.path.dirname(os.path.abspath(__file__))
        ui_path += '\\Bibli_ui\\ecrandeveloppeur.ui'
        loadUi(ui_path, self)

    def setup_logics(self, w_parent):
        bd_config = ECRAN_DEV.get_bd_credentials(self)
                #Try 
        mysql_app_connection(bd_config, True)
     

        mysql_app_create_tables()
        inserer_livres()
        inserer_selection_chapitre()

    

    def get_bd_credentials(self):

        conn_fields = {}
        conn_fields['host'] = 'localhost'
        conn_fields['port'] = '3306'
        conn_fields['user'] = 'root' #TODO: Faire un user juste pour cette BD
        conn_fields['password'] = 'mysql' #TODO: Temporaire pour le développement

        return conn_fields

    def connect_actionbtn(self):

        pass

class ECRAN_CHAPITRE(QDialog):

    def __init__(self):
        super(ECRAN_CHAPITRE, self).__init__()
        ui_path =  os.path.dirname(os.path.abspath(__file__))
        ui_path += '\\Bibli_ui\\selectionchapitres.ui'
        loadUi(ui_path, self)

    def setup_logics(self, w_parent):
        self.field_selection_chapitre()
        #self.connectionbtn.clicked.connect(lambda:self.connect_actionbtn())
        pass

    def field_selection_chapitre(self):

        chapitres = lister_chapitre()
        index = 0
        for champs in chapitres:
            self.selection_chapitre_comboBox.addItem("")
            self.selection_chapitre_comboBox.setItemText(index, "chapitre " + str(champs[2]))
            index +=1
            


   