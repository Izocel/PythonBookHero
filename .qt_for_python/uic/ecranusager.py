# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\OneDrive - Cégep de Victoriaville\TransfertSchool\2021-2022\BD-2\PythonBookHero\BookHeroProjectDesigner\ecranusager.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
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
        self.groupBox_5 = QtWidgets.QGroupBox(self.bgwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setStyleSheet("border: none;")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setStyleSheet("boder: none;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.label_courriel_2 = QtWidgets.QLabel(self.groupBox_2)
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setAutoFillBackground(False)
        self.pushButton_13.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_3.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setAutoFillBackground(False)
        self.pushButton_14.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_3.addWidget(self.pushButton_14)
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy)
        self.pushButton_20.setAutoFillBackground(False)
        self.pushButton_20.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_20.setObjectName("pushButton_20")
        self.horizontalLayout_3.addWidget(self.pushButton_20)
        self.pushButton_23 = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy)
        self.pushButton_23.setAutoFillBackground(False)
        self.pushButton_23.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_23.setObjectName("pushButton_23")
        self.horizontalLayout_3.addWidget(self.pushButton_23)
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy)
        self.pushButton_22.setAutoFillBackground(False)
        self.pushButton_22.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_22.setObjectName("pushButton_22")
        self.horizontalLayout_3.addWidget(self.pushButton_22)
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy)
        self.pushButton_21.setAutoFillBackground(False)
        self.pushButton_21.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_21.setObjectName("pushButton_21")
        self.horizontalLayout_3.addWidget(self.pushButton_21)
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setAutoFillBackground(False)
        self.pushButton_12.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_3.addWidget(self.pushButton_12)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_courriel = QtWidgets.QLabel(self.groupBox_4)
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
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setAutoFillBackground(False)
        self.pushButton_15.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout.addWidget(self.pushButton_15)
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy)
        self.pushButton_19.setAutoFillBackground(False)
        self.pushButton_19.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.verticalLayout.addWidget(self.pushButton_19)
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.pushButton_18.setAutoFillBackground(False)
        self.pushButton_18.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_18.setObjectName("pushButton_18")
        self.verticalLayout.addWidget(self.pushButton_18)
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setAutoFillBackground(False)
        self.pushButton_17.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.verticalLayout.addWidget(self.pushButton_17)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_6.addWidget(self.groupBox_4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.deconnectionpushButton = QtWidgets.QPushButton(self.groupBox_3)
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
        self.deconnectionpushButton.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(200, 200, 200);\n"
"")
        self.deconnectionpushButton.setObjectName("deconnectionpushButton")
        self.horizontalLayout_4.addWidget(self.deconnectionpushButton)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.horizontalLayout_5.addWidget(self.groupBox_5)
        self.verticalLayout_3.addWidget(self.bgwidget)

        self.retranslateUi(EcranUsager)
        QtCore.QMetaObject.connectSlotsByName(EcranUsager)

    def retranslateUi(self, EcranUsager):
        _translate = QtCore.QCoreApplication.translate
        EcranUsager.setWindowTitle(_translate("EcranUsager", "Dialog"))
        self.label.setText(_translate("EcranUsager", "Python Book Hero"))
        self.label_courriel_2.setText(_translate("EcranUsager", "Livres"))
        self.pushButton_13.setText(_translate("EcranUsager", "PushButton"))
        self.pushButton_14.setText(_translate("EcranUsager", "PushButton"))
        self.pushButton_20.setText(_translate("EcranUsager", "PushButton"))
        self.pushButton_23.setText(_translate("EcranUsager", "PushButton"))
        self.pushButton_22.setText(_translate("EcranUsager", "PushButton"))
        self.pushButton_21.setText(_translate("EcranUsager", "PushButton"))
        self.pushButton_12.setText(_translate("EcranUsager", "PushButton"))
        self.label_courriel.setText(_translate("EcranUsager", "Sauvegardes"))
        self.pushButton_15.setText(_translate("EcranUsager", "PushButton"))
        self.pushButton_19.setText(_translate("EcranUsager", "PushButton"))
        self.pushButton_18.setText(_translate("EcranUsager", "PushButton"))
        self.pushButton_17.setText(_translate("EcranUsager", "PushButton"))
        self.deconnectionpushButton.setText(_translate("EcranUsager", "déconnection"))
