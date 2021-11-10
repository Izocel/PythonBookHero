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
        windowsGeo = QtCore.QRect(m.x, m.y, w, h)
        loginGeo = QtCore.QRect(m.x, m.y, w33, h75)

#ref: https://stackoverflow.com/questions/4528347/clear-all-widgets-in-a-layout-in-pyqt
def clearLayout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()


# Workspace Related #
from gestion_ui import *




############################################ CLASSES DE DIALOGUES ############################################

############################## MyStackedWidget ##############################
# Extension de la classe provenant de QStackedWidget
# Proprietées connu sur MyStackedWidget
    # connected_id
    # ?
    # ?
#
class MyStackedWidget(QStackedWidget):
    

    connected_id:int = 0
    logged_in:bool = False

    def get_connected_id(self) -> int:
        return self.connected_id
    def set_connected_id(self, id:int) -> None:
        self.connected_id = id


    def get_logged_in(self) -> bool:
        return self.logged_in
    def set_logged_in(self, state:bool) -> None:
        self.logged_in = state
    

    def __init__(self):
        super(MyStackedWidget, self).__init__()
        self.settings = QSettings('MOMO-RVÐ', 'Python Book Hero')

        try:
            self.resize(self.settings.value('window size'))
            self.move(self.settings.value('window position'))
            self.setCurrentIndex(self.settings.value('last index'))
        except:
            print("An exception occurred")
        finally:
            pass
    
    def closeEvent(self,a0: QtGui.QCloseEvent) -> None:
        self.settings.setValue('window size', self.size())
        self.settings.setValue('window position', self.pos())
        self.settings.setValue('last index', self.currentIndex())

        return super().closeEvent(a0)

    def switchTo(self,child_name:str, child_class:QDialog = QDialog)-> int:
        child = self.findChild(child_class, child_name)
        index:int = self.indexOf(child)
        try:
            self.setCurrentIndex(index)
        except:
            print("Unable to find that child")
            return -1
        return index



############################## ECRAN_USAGER ##############################
# Extension de la classe provenant du designer (ecranusager.ui)
# Proprietées connu sur ECRAN_USAGER
    # deconnectionpushButton
    # ?
    # ?
#
class ECRAN_USAGER(QDialog):

    parent:MyStackedWidget

    def __init__(self) -> None:
        super(ECRAN_USAGER, self).__init__()
        ui_path =  os.path.dirname(os.path.abspath(__file__))
        ui_path += '\\Bibli_ui\\ecranusager.ui'
        loadUi(ui_path, self)

    def setup_logics(self, w_parent:MyStackedWidget) -> None:
        self.parent = w_parent
        self.deconnectionpushButton.clicked.connect(lambda:self.deconnection_usagers_btnaction())

    def deconnection_usagers_btnaction(self):
        ecran_acceuil:ECRAN_ACCEUIL = self.parent.findChild(QDialog, 'EcranAcceuil')
        ecran_acceuil.app_disconnect()
        ecran_acceuil.setup_logics(self.parent)
        self.parent.switchTo('EcranAcceuil')
        self.parent.showNormal()

    def fetch_livre(self, usager_id:int) -> None:
        livres_user = liste_livre_usager(usager_id)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        _translate = QtCore.QCoreApplication.translate

        layout:QtWidgets.QHBoxLayout = self.LivreshorizontalLayout
        clearLayout(layout)

        ecran_chapitre:ECRAN_CHAPITRE = self.parent.findChild(QDialog, 'EcranChapitres')

        i = 0
        for livre in livres_user:
            id_livre = livre[0]
            nomLivre = livre[1]
            auteurLivre = livre[2]

            if(i >0):
                sizePolicy.setHeightForWidth(self.livrespushButton.sizePolicy().hasHeightForWidth())
            self.livrespushButton = QtWidgets.QPushButton(self.sectionHaut_groupBox)
            self.livrespushButton.setSizePolicy(sizePolicy)
            self.livrespushButton.setAutoFillBackground(False)
            self.livrespushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.livrespushButton.setStyleSheet(":!active, :active{font-size:32px;border-radius:20px;\n""background-color: rgb(170, 255, 255);\n"
            "}\n"":hover{\n""background-color: rgb(23, 250, 250);\n""}")
            self.livrespushButton.setText(_translate("EcranUsager", f"{nomLivre} \n {auteurLivre}"))
            
            self.livrespushButton.clicked.connect(lambda:ecran_chapitre.field_selection_chapitre(id_livre))
            layout.addWidget(self.livrespushButton)
           
            i+=1

    def refresh_ui(self):
        if(self.parent.get_logged_in()):
            user_id:int = self.parent.get_connected_id()
            self.fetch_livre(user_id)
            self.fetch_saves(user_id)

    def fetch_saves(self, usager_id:int) -> 0:
        saves = lister_sauvegardes_usager(usager_id)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        _translate = QtCore.QCoreApplication.translate

        layout:QtWidgets.QVBoxLayout = self.SavesverticalLayout
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
            layout.addWidget(self.savespushButton)
            self.savespushButton.setText(_translate("EcranUsager", f"{saveString}"))
            i+= 1


#### ECRAN_ACCEUIL ##############################################
# Extension de la classe provenant du designer (ecranacceuil.ui)
# Proprietées connu sur ECRAN_ACCEUIL
    # connectionpushButton (btn)
    # motdepasse_lineEdit (input)
    # courriel_lineEdit (input)
    # label_mauvaise_infos (label)
#
class ECRAN_ACCEUIL(QDialog):

    parent:MyStackedWidget

    def __init__(self):
        super(ECRAN_ACCEUIL, self).__init__()
        ui_path =  os.path.dirname(os.path.abspath(__file__))
        ui_path += '\\Bibli_ui\\ecranacceuil.ui'
        loadUi(ui_path, self)

    def setup_logics(self, w_parent:MyStackedWidget):
        self.parent = w_parent
        self.label_mauvaise_infos.hide()
        self.connectionpushButton.clicked.connect(lambda:self.connection_usagers_btnaction())

    
    def app_disconnect(self):
        connected = self.parent.get_logged_in()
        
        if(connected):
            connected = not mysql_app_disconnection()

        if( not connected ):
            self.parent.set_logged_in(False)
            self.parent.set_connected_id(0)

        return connected
        
    def app_connect(self):

        bd_config = self.get_bd_credentials()

        if(mysql_app_connection(bd_config, True)):
            self.parent.set_logged_in(True)

            mysql_app_create_tables()
            mysql_app_insert_user()
            inserer_livres()
            inserer_chapitres_livres()
            attribuer_livre_par_default()

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
        connected = self.parent.get_logged_in()

        if(not connected):
            self.app_connect()
            connected = self.parent.get_logged_in()

        if(connected):
            user_cred = self.get_usager_credentials()
            acces_usager_promu = verif_connection_usager(**user_cred)

            if(acces_usager_promu):
                user_id:int = acces_usager_promu[0]
                self.parent.set_connected_id(user_id)
                ecran_usager:ECRAN_USAGER = self.parent.findChild(QDialog, 'EcranUsager')
                ecran_usager.refresh_ui()

                self.label_mauvaise_infos.hide()
                self.connectionpushButton.disconnect()

                ######### CHANGER DE PAGE  ############
                self.parent.switchTo('EcranUsager')
                self.parent.showMaximized()

            else: # Ajouter un message à l'écran de mauvaise infos....
                self.app_disconnect()
                self.label_mauvaise_infos.show()
            
#### ECRAN_CHAPITRE ##############################################
# Extension de la classe provenant du designer (ecranchapitre.ui)
# Proprietées connu sur ECRAN_CHAPITRE
    # selection_chapitre_comboBox_2
    # ecran_affichage_chapitre_textBrowser
    # ?
#
class ECRAN_CHAPITRE(QDialog):

    parent:MyStackedWidget

    def __init__(self):
        super(ECRAN_CHAPITRE, self).__init__()
        ui_path =  os.path.dirname(os.path.abspath(__file__))
        ui_path += '\\Bibli_ui\\selectionchapitres.ui'
        loadUi(ui_path, self)

    def setup_logics(self, w_parent:MyStackedWidget):
        self.parent = w_parent
        self.retour_accueil_pushButton.clicked.connect(lambda: self.call_home())
        self.page_precedente_pushButton_2.clicked.connect(lambda: self.prev_chapitre())
        self.page_suivante_pushButton_3.clicked.connect(lambda: self.next_chapitre())
        pass

    def call_home(self):
        ecran_usager:ECRAN_USAGER = self.parent.findChild(ECRAN_USAGER, 'EcranUsager')
        ecran_usager.refresh_ui()
        self.parent.switchTo('EcranUsager')

    def next_chapitre(self):
        chapitres_comboBox:QtWidgets.QComboBox = self.selection_chapitre_comboBox_2
        max = chapitres_comboBox.count()-1
        nextIndex = chapitres_comboBox.currentIndex()+1

        if(nextIndex <= max):
            chapitres_comboBox.setCurrentIndex(nextIndex)

    def prev_chapitre(self):
        chapitres_comboBox:QtWidgets.QComboBox = self.selection_chapitre_comboBox_2
        prevIndex = chapitres_comboBox.currentIndex()-1

        if(prevIndex >= 1):
            chapitres_comboBox.setCurrentIndex(prevIndex)

    def field_selection_chapitre(self, id_livre:int):

        chapitres_comboBox:QtWidgets.QComboBox = self.selection_chapitre_comboBox_2
        chapitres_comboBox.clear()

        self.parent.switchTo(self.objectName())
        self.page_precedente_pushButton_2.hide()

        dict_chapitre = lister_chapitre(id_livre)
        
      
        chapitres_comboBox.addItem("")
        chapitres_comboBox.setItemText(0, "Sélectionnez un chapitre")
        chapitres_comboBox.currentIndexChanged.connect(lambda:self.selectionchange())

        if(len(dict_chapitre) > 0):

            index = 0
            for chapitre in dict_chapitre:

                index += 1
                if(len(chapitre) > 0):

                    if (index == 1):
                        chapitres_comboBox.addItem("")
                        chapitres_comboBox.setItemText(index, "Introduction-Règlements")

                    else:
                        numero_chapitre = str(chapitre[2])
                        chapitres_comboBox.addItem("")
                        chapitres_comboBox.setItemText(index, "Chapitre " + numero_chapitre)
                        
                else:
                    chapitres_comboBox.addItem("")
                    chapitres_comboBox.setItemText(index, "Nous somme désolés, aucune données disponible")
            chapitres_comboBox.setCurrentIndex(1)

    def check_next_prev_btn(self) -> int:

        chapitres_comboBox:QtWidgets.QComboBox = self.selection_chapitre_comboBox_2
        maxindex = chapitres_comboBox.count()-1
        prevBtn:QtWidgets.QPushButton = self.page_precedente_pushButton_2
        nextBtn:QtWidgets.QPushButton = self.page_suivante_pushButton_3

        if(chapitres_comboBox.currentIndex() <= 1):
            prevBtn.hide()
        else:
            prevBtn.show()

        if(chapitres_comboBox.currentIndex() == maxindex):
            nextBtn.hide()   
        else:
             nextBtn.show()
            
        return maxindex +1


    def selectionchange(self):
        
        self.check_next_prev_btn()

        _translate = QtCore.QCoreApplication.translate
        index = self.selection_chapitre_comboBox_2.currentIndex()
        index -=1
            
        txt_default:str = "Veuillez selectionner un chapitre..."


        if(index >= 0):
            chapitre = field_fenetre_chapitre(index)
            contenue = chapitre[0][3]

            # //// AFFICHAGE ////
            txt_browser:QtWidgets.QTextBrowser = self.ecran_affichage_chapitre_textBrowser
            txt_browser.setHtml(_translate("EcranChapitres", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
            f"{contenue}</body></html>"))
        else:
            txt_browser:QtWidgets.QTextBrowser = self.ecran_affichage_chapitre_textBrowser
            txt_browser.setHtml(_translate("EcranChapitres", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
            f"{txt_default}</body></html>"))