# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BookHeroProjectDesigner/ecranacceuil.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EcranDeveloppeur(object):
    def setupUi(self, EcranDeveloppeur):
        EcranDeveloppeur.setObjectName("EcranDeveloppeur")
        EcranDeveloppeur.resize(1426, 903)
        self.bgwidget = QtWidgets.QWidget(EcranDeveloppeur)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 1451, 911))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"background: qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(100, 25, 2, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.bgwidget.setObjectName("bgwidget")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(270, 140, 921, 71))
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(520, 230, 391, 41))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";color:rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.connectionbtn = QtWidgets.QPushButton(self.bgwidget)
        self.connectionbtn.setGeometry(QtCore.QRect(510, 390, 341, 51))
        self.connectionbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.connectionbtn.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.connectionbtn.setObjectName("connectionbtn")
        self.error = QtWidgets.QLabel(self.bgwidget)
        self.error.setGeometry(QtCore.QRect(440, 456, 341, 20))
        self.error.setStyleSheet("font: 12pt \"MS Shell Dlg 2\"; color:red;")
        self.error.setText("")
        self.error.setObjectName("error")
        self.passwordfield = QtWidgets.QLineEdit(self.bgwidget)
        self.passwordfield.setGeometry(QtCore.QRect(520, 310, 341, 51))
        self.passwordfield.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.passwordfield.setObjectName("passwordfield")
        self.label_6 = QtWidgets.QLabel(self.bgwidget)
        self.label_6.setGeometry(QtCore.QRect(520, 290, 81, 20))
        self.label_6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(EcranDeveloppeur)
        QtCore.QMetaObject.connectSlotsByName(EcranDeveloppeur)

    def retranslateUi(self, EcranDeveloppeur):
        _translate = QtCore.QCoreApplication.translate
        EcranDeveloppeur.setWindowTitle(_translate("EcranDeveloppeur", "Dialog"))
        self.label.setText(_translate("EcranDeveloppeur", "Python Book Hero (écran hors production)"))
        self.label_2.setText(_translate("EcranDeveloppeur", "Entrer le mot de passe de la BD"))
        self.connectionbtn.setText(_translate("EcranDeveloppeur", "Connection"))
        self.passwordfield.setText(_translate("EcranDeveloppeur", "********"))
        self.label_6.setText(_translate("EcranDeveloppeur", "Mot de passe"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EcranDeveloppeur = QtWidgets.QDialog()
    ui = Ui_EcranDeveloppeur()
    ui.setupUi(EcranDeveloppeur)
    EcranDeveloppeur.show()
    sys.exit(app.exec_())
