# Workspace related
from instances_ui import *


#################################### Section LAUNCH ####################################

class MyStackedWidget(QStackedWidget):

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


###################### Section de BD (à venir) ###################### 



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

# Ajput des widgets 'layers'
s_widgets.setGeometry(loginGeo)
s_widgets.addWidget(ecran_acceuil)
s_widgets.addWidget(ecran_usager)
s_widgets.addWidget(ecran_chapitre)

s_widgets.show()

sys.exit(App.exec_())