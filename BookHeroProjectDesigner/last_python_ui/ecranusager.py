# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BookHeroProjectDesigner/ecranusager.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EcranUsager(object):
    def setupUi(self, EcranUsager):
        EcranUsager.setObjectName("EcranUsager")
        EcranUsager.resize(1400, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EcranUsager.sizePolicy().hasHeightForWidth())
        EcranUsager.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(EcranUsager)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bgwidget = QtWidgets.QWidget(EcranUsager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bgwidget.sizePolicy().hasHeightForWidth())
        self.bgwidget.setSizePolicy(sizePolicy)
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"background: qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(100, 25, 2, 255), stop:1 rgba(255, 255, 255, 255));}\n"
"")
        self.bgwidget.setObjectName("bgwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.bgwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.main_groupBox = QtWidgets.QGroupBox(self.bgwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_groupBox.sizePolicy().hasHeightForWidth())
        self.main_groupBox.setSizePolicy(sizePolicy)
        self.main_groupBox.setStyleSheet("border: none;")
        self.main_groupBox.setTitle("")
        self.main_groupBox.setObjectName("main_groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.main_groupBox)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.sectionHaut_groupBox = QtWidgets.QGroupBox(self.main_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sectionHaut_groupBox.sizePolicy().hasHeightForWidth())
        self.sectionHaut_groupBox.setSizePolicy(sizePolicy)
        self.sectionHaut_groupBox.setStyleSheet("")
        self.sectionHaut_groupBox.setTitle("")
        self.sectionHaut_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.sectionHaut_groupBox.setFlat(False)
        self.sectionHaut_groupBox.setObjectName("sectionHaut_groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.sectionHaut_groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.sectionHaut_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.label_courriel_2 = QtWidgets.QLabel(self.sectionHaut_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_courriel_2.sizePolicy().hasHeightForWidth())
        self.label_courriel_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_courriel_2.setFont(font)
        self.label_courriel_2.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";\n"
"color: #fff;")
        self.label_courriel_2.setObjectName("label_courriel_2")
        self.verticalLayout_4.addWidget(self.label_courriel_2)
        self.LivreshorizontalLayout = QtWidgets.QHBoxLayout()
        self.LivreshorizontalLayout.setObjectName("LivreshorizontalLayout")
        self.verticalLayout_4.addLayout(self.LivreshorizontalLayout)
        self.verticalLayout_6.addWidget(self.sectionHaut_groupBox)
        self.sectionMillieu_groupBox = QtWidgets.QGroupBox(self.main_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sectionMillieu_groupBox.sizePolicy().hasHeightForWidth())
        self.sectionMillieu_groupBox.setSizePolicy(sizePolicy)
        self.sectionMillieu_groupBox.setTitle("")
        self.sectionMillieu_groupBox.setObjectName("sectionMillieu_groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.sectionMillieu_groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_courriel = QtWidgets.QLabel(self.sectionMillieu_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_courriel.sizePolicy().hasHeightForWidth())
        self.label_courriel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_courriel.setFont(font)
        self.label_courriel.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";\n"
"color: #fff;")
        self.label_courriel.setObjectName("label_courriel")
        self.verticalLayout_5.addWidget(self.label_courriel)
        self.SavesverticalLayout = QtWidgets.QVBoxLayout()
        self.SavesverticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.SavesverticalLayout.setObjectName("SavesverticalLayout")
        self.verticalLayout_5.addLayout(self.SavesverticalLayout)
        self.verticalLayout_6.addWidget(self.sectionMillieu_groupBox)
        self.sectionBas_groupBox = QtWidgets.QGroupBox(self.main_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sectionBas_groupBox.sizePolicy().hasHeightForWidth())
        self.sectionBas_groupBox.setSizePolicy(sizePolicy)
        self.sectionBas_groupBox.setTitle("")
        self.sectionBas_groupBox.setObjectName("sectionBas_groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.sectionBas_groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.deconnectionpushButton = QtWidgets.QPushButton(self.sectionBas_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deconnectionpushButton.sizePolicy().hasHeightForWidth())
        self.deconnectionpushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.deconnectionpushButton.setFont(font)
        self.deconnectionpushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deconnectionpushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.deconnectionpushButton.setStyleSheet(":!active ,:active{border: 1px; border-radius:20px; background-color: rgb(240, 110, 100);}\n"
":hover{background-color: rgb(210, 50, 50);}")
        self.deconnectionpushButton.setObjectName("deconnectionpushButton")
        self.horizontalLayout_4.addWidget(self.deconnectionpushButton)
        self.verticalLayout_6.addWidget(self.sectionBas_groupBox)
        self.horizontalLayout_5.addWidget(self.main_groupBox)
        self.verticalLayout_3.addWidget(self.bgwidget)

        self.retranslateUi(EcranUsager)
        QtCore.QMetaObject.connectSlotsByName(EcranUsager)

    def retranslateUi(self, EcranUsager):
        _translate = QtCore.QCoreApplication.translate
        EcranUsager.setWindowTitle(_translate("EcranUsager", "Dialog"))
        self.label.setText(_translate("EcranUsager", "Python Book Hero"))
        self.label_courriel_2.setText(_translate("EcranUsager", "Livres"))
        self.label_courriel.setText(_translate("EcranUsager", "Sauvegardes"))
        self.deconnectionpushButton.setText(_translate("EcranUsager", "déconnection"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EcranUsager = QtWidgets.QDialog()
    ui = Ui_EcranUsager()
    ui.setupUi(EcranUsager)
    EcranUsager.show()
    sys.exit(app.exec_())
