import sys

# Workspace related
from instances_ui import *


# Section LAUNCH ##############################################


# Section de BD......



# instance de la couche applicative
App = QApplication(sys.argv)
s_widgets = QStackedWidget()


##### Définir les classes d'instances dans instances_ui.py #####

# instance 1 ......
ecran_acceuil = ECRAN_ACCEUIL()
ecran_acceuil.setup_logics(s_widgets)


# instance 2 .......
ecran_usager = ECRAN_USAGER()
ecran_usager.setup_logics(s_widgets)

# Ajput des widgets 'layers'
s_widgets.setGeometry(ecran_acceuil.geometry())
s_widgets.addWidget(ecran_acceuil)
s_widgets.addWidget(ecran_usager)
s_widgets.show()

sys.exit(App.exec_())