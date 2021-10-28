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
class ECRAN_ACCEUIL(QDialog):

    def __init__(self):
        super(ECRAN_ACCEUIL, self).__init__()
        ui_path =  os.path.dirname(os.path.abspath(__file__))
        ui_path += '\\Bibli_ui\\ecranacceuil.ui'
        loadUi(ui_path, self)

    def setup_logics(self, w_parent):
        self.connectionbtn.clicked.connect(lambda:self.connect_actionbtn(w_parent))