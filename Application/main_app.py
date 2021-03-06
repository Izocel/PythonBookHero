# Workspace related
from instances_ui import *


#################################### Section LAUNCH ####################################

# instance de la couche applicative
App = QApplication(sys.argv)
s_widgets = MyStackedWidget()
s_widgets.setObjectName("Python book hero")

##### Définir les classes d'instances dans instances_ui.py #####

# instance 1 ......
ecran_acceuil = ECRAN_ACCEUIL()
ecran_acceuil.setup_logics(s_widgets)

# instance 2 .......
ecran_usager = ECRAN_USAGER()
ecran_usager.setup_logics(s_widgets)

# instance 3 .......
ecran_chapitre = ECRAN_CHAPITRE()
ecran_chapitre.setup_logics(s_widgets)


# Ajout des widgets 'layers'
s_widgets.setGeometry(loginGeo)
s_widgets.addWidget(ecran_acceuil)
s_widgets.addWidget(ecran_usager)
s_widgets.addWidget(ecran_chapitre)


s_widgets.show()
sys.exit(App.exec_())