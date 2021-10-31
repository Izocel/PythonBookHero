import sys

# Workspace related
from instances_ui import *


# Section LAUNCH ##############################################

# instance de la couche applicative
App = QApplication(sys.argv)
s_widgets = QStackedWidget()


##### Définir les classes d'instances dans instances_ui.py #####

# instance 1 ......
ecran_dev = ECRAN_DEV()
ecran_dev.setup_logics(s_widgets)

# instance 2 .......
ecran_chapitre = ECRAN_CHAPITRE()
ecran_chapitre.setup_logics(s_widgets)

# Ajput des widgets 'layers'
s_widgets.setGeometry(ecran_dev.geometry())
s_widgets.addWidget(ecran_chapitre)
s_widgets.addWidget(ecran_dev)
s_widgets.show()

sys.exit(App.exec_())