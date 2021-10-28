import sys

# Workspace related
from instances_ui import *


# Section LAUNCH ##############################################

# instance de la couche applicative
App = QApplication(sys.argv)
s_widgets = QStackedWidget()

# instance 1 ......
# Définir les classes dans instances_ui.py
ecran_acceuil = ECRAN_ACCEUIL()
ecran_acceuil.setup_logics(s_widgets)


# instance 2 .......


# Ajput des widgets 'layers'
s_widgets.setGeometry(ecran_acceuil.geometry())
s_widgets.addWidget(ecran_acceuil)
s_widgets.show()

sys.exit(App.exec_())