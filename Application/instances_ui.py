import os

# PyQt5 Base #
from PyQt5 import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSettings

# Primary monitor infos #
from screeninfo import get_monitors
for m in get_monitors():
    x= int(m.x)
    y = int(m.y)
    w= int(m.width)
    h = int(m.height)
    w33 = int(w/3)
    h75 = int(h/1.5)
    if(m.is_primary):
        windowsGeo = QtCore.QRect(m.x, m.y+25, w, h-30)
        loginGeo = QtCore.QRect(m.x, m.y+25, w33, h75)

#ref: https://stackoverflow.com/questions/4528347/clear-all-widgets-in-a-layout-in-pyqt
def clearLayout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()


# Workspace Related #
from gestion_ui import *




############################################ CLASSES DE DIALOGUES ############################################

############################## ECRAN_USAGER ##############################
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
        parent.setGeometry(loginGeo)

    def fetch_livre(self, usager_id:int) -> None:
        livres_user = liste_livre_usager(usager_id)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        _translate = QtCore.QCoreApplication.translate
        ecran_chapitre = parent.findChild(QDialog, 'EcranChapitres')
        ecran_chapitre.field_selection_chapitre(1)

        layout = self.LivreshorizontalLayout
        clearLayout(layout)

        i = 0
        for livre in livres_user:
            nomLivre = livre[1]
            auteurLivre = livre[2]
            if(i >0):
                sizePolicy.setHeightForWidth(self.livrespushButton.sizePolicy().hasHeightForWidth())
            self.livrespushButton = QtWidgets.QPushButton(self.sectionHaut_groupBox)
            self.livrespushButton.setSizePolicy(sizePolicy)
            self.livrespushButton.setAutoFillBackground(False)
            self.livrespushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.livrespushButton.setStyleSheet(":active{font-size:32px;border-radius:20px;\n""background-color: rgb(170, 255, 255);\n"
            "}\n"":hover{\n""background-color: rgb(23, 250, 250);\n""}")
            self.LivreshorizontalLayout.addWidget(self.livrespushButton)
            self.livrespushButton.setText(_translate("EcranUsager",
            f"{nomLivre} \n {auteurLivre}"))
            i+=1



    def fetch_saves(self, usager_id:int) -> 0:
        saves = lister_sauvegardes_usager(usager_id)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        _translate = QtCore.QCoreApplication.translate

        layout = self.SavesverticalLayout
        clearLayout(layout)

        i = 0
        for save in saves:
            
            dt_string = save[3].strftime("%c")
            titre = save[4].title()
            num_chapitre = save[1]

            if(num_chapitre == 0):
                num_chapitre = 'Introduction'
            else:
                num_chapitre = "Ch."+str(num_chapitre)

            saveString = f"-{i+1} {titre} |{num_chapitre}| {dt_string}"
            # TODO:
            #fonction backend qui renvoi le string d'affichage des saves params(usager_id, str_separator)
            if(i >0):
                sizePolicy.setHeightForWidth(self.savespushButton.sizePolicy().hasHeightForWidth())
            self.savespushButton = QtWidgets.QPushButton(self.sectionHaut_groupBox)
            self.savespushButton.setSizePolicy(sizePolicy)
            self.savespushButton.setAutoFillBackground(False)
            self.savespushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.savespushButton.setStyleSheet(":active, :!active{font-size:32px;border-radius:20px;\n""background-color: rgb(170, 255, 255);\n"
            "}\n"":hover{\n""background-color: rgb(23, 250, 250);\n""}")
            self.SavesverticalLayout.addWidget(self.savespushButton)
            self.savespushButton.setText(_translate("EcranUsager",
            f"{saveString}"))
            i+= 1


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
            inserer_livres()
            inserer_chapitres_livres()
            attribuer_livre_par_default()
            
            
        return logged_in

    def get_bd_credentials(self):

        conn_fields = {}
        conn_fields['host'] = 'localhost'
        conn_fields['port'] = '3306'
        conn_fields['user'] = 'root' #TODO: Faire un user juste pour cette BD
        conn_fields['password'] = '@mysqlroot2022'  #getpass("Entrer le mot de passe mysql: \n ==> ")

        return conn_fields

    def get_usager_credentials(self):

        conn_fields = {}
        conn_fields['courriel'] = self.courriel_lineEdit.text()
        conn_fields['hashmotpasse'] = hash_sha2_data([self.motdepasse_lineEdit.text()])[0]

        return conn_fields

    def connection_usagers_btnaction(self) -> None:
        global logged_in

        if(not logged_in):
            logged_in = self.app_connect()

        if(logged_in):
            user_cred = self.get_usager_credentials()
            acces_usager_promu = verif_connection_usager(**user_cred)

            if(acces_usager_promu):
                user_id = acces_usager_promu[0]
                ecran_usager = parent.findChild(QDialog, 'EcranUsager')
                ecran_usager.fetch_livre(user_id)
                ecran_usager.fetch_saves(user_id)

                self.label_mauvaise_infos.hide()
                self.connectionpushButton.disconnect()

                ######### CHANGER DE PAGE  ############
                parent.setCurrentIndex(parent.currentIndex()+1)
                parent.setGeometry(windowsGeo)
                parent.showMaximized()

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
        #self.field_selection_chapitre() ## Migrer vers une autre appel ou changer son setup_logics() de place...
        #self.connectionbtn.clicked.connect(lambda:self.connect_actionbtn())
        pass

    def field_selection_chapitre(self, id_livre:int):

        dict_chapitre = lister_chapitre(id_livre)

        self.selection_chapitre_comboBox_2.addItem("")
        self.selection_chapitre_comboBox_2.setItemText(0, "Sélectionnez un chapitre")
        self.selection_chapitre_comboBox_2.currentIndexChanged.connect(self.selectionchange)

        if(len(dict_chapitre) > 0):

            index = 0
            for chapitre in dict_chapitre:

                index += 1
                if(len(chapitre) > 0):
                    

                    if (index == 1):
                        self.selection_chapitre_comboBox_2.addItem("")
                        self.selection_chapitre_comboBox_2.setItemText(index, "Introduction-Règlements")

                    else:
                        numero_chapitre = str(chapitre[2])
                        self.selection_chapitre_comboBox_2.addItem("")
                        self.selection_chapitre_comboBox_2.setItemText(index, "Chapitre " + numero_chapitre)
                        
                else:
                    self.selection_chapitre_comboBox_2.addItem("")
                    self.selection_chapitre_comboBox_2.setItemText(index, "Nous somme désolés, aucune données disponible")
        
    
    def selectionchange(self):
        _translate = QtCore.QCoreApplication.translate
        index = self.selection_chapitre_comboBox_2.currentIndex()
        index -=1
        if(index >= 0):
            chapitre = field_fenetre_chapitre(index)
            contenue = chapitre[0][3]

            # //// AFFICHAGE ////
            txt_browser = self.ecran_affichage_chapitre_textBrowser
            txt_browser.setHtml(_translate("EcranChapitres", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
            f"{contenue}</body></html>"))