import os
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
        self.connectionbtn.clicked.connect(lambda:self.connect_actionbtn())
    

    def get_bd_credentials(self):

        conn_fields = {}
        conn_fields['host'] = 'localhost'
        conn_fields['port'] = '3306'
        conn_fields['user'] = 'root' #TODO: Faire un user juste pour cette BD
        conn_fields['password'] = self.passwordfield.text() #TODO: Temporaire pour le développement

        return conn_fields

    def connect_actionbtn(self):

        bd_config = ECRAN_DEV.get_bd_credentials(self)
        #Try 
        mysql_app_connection(bd_config, True)
        self.connectionbtn.clicked.disconnect()

        mysql_app_create_tables()