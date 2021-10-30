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
ecran_dev = ECRAN_DEV()
ecran_dev.setup_logics(s_widgets)


# instance 2 .......


# Ajput des widgets 'layers'
s_widgets.setGeometry(ecran_dev.geometry())
s_widgets.addWidget(ecran_dev)
s_widgets.show()

sys.exit(App.exec_())