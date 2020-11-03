# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VtnaConfig.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Configuracion(object):
    def setupUi(self, Configuracion):
        if not Configuracion.objectName():
            Configuracion.setObjectName(u"Configuracion")
        Configuracion.resize(1366, 700)
        self.listView = QListView(Configuracion)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(400, 58, 256, 401))
        self.radioButton_3 = QRadioButton(Configuracion)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(90, 218, 151, 41))
        font = QFont()
        font.setFamily(u"DejaVu Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.radioButton = QRadioButton(Configuracion)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(90, 68, 131, 51))
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.push_Menu = QPushButton(Configuracion)
        self.push_Menu.setObjectName(u"push_Menu")
        self.push_Menu.setGeometry(QRect(1040, 468, 160, 80))
        font1 = QFont()
        font1.setFamily(u"Arial Black")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.push_Menu.setFont(font1)
        icon = QIcon()
        icon.addFile(u"MainW/icon/home.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Menu.setIcon(icon)
        self.push_Menu.setIconSize(QSize(60, 60))
        self.push_Menu.setAutoDefault(False)
        self.label = QLabel(Configuracion)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(386, 20, 241, 41))
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.push_Desactivar = QPushButton(Configuracion)
        self.push_Desactivar.setObjectName(u"push_Desactivar")
        self.push_Desactivar.setGeometry(QRect(210, 340, 111, 51))
        font2 = QFont()
        font2.setFamily(u"Arial Black")
        font2.setBold(True)
        font2.setWeight(75)
        self.push_Desactivar.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u"MainW/icon/cancelar2.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Desactivar.setIcon(icon1)
        self.push_Desactivar.setIconSize(QSize(20, 20))
        self.push_Desactivar.setAutoDefault(False)
        self.radioButton_2 = QRadioButton(Configuracion)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(90, 138, 131, 51))
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.listView_2 = QListView(Configuracion)
        self.listView_2.setObjectName(u"listView_2")
        self.listView_2.setGeometry(QRect(340, 58, 61, 401))
        self.push_Activar = QPushButton(Configuracion)
        self.push_Activar.setObjectName(u"push_Activar")
        self.push_Activar.setGeometry(QRect(70, 340, 111, 51))
        self.push_Activar.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u"MainW/icon/check.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Activar.setIcon(icon2)
        self.push_Activar.setIconSize(QSize(20, 20))
        self.push_Activar.setAutoDefault(False)

        self.retranslateUi(Configuracion)

        QMetaObject.connectSlotsByName(Configuracion)
    # setupUi

    def retranslateUi(self, Configuracion):
        Configuracion.setWindowTitle(QCoreApplication.translate("Configuracion", u"Dialog", None))
        self.radioButton_3.setText(QCoreApplication.translate("Configuracion", u"Vendedores", None))
        self.radioButton.setText(QCoreApplication.translate("Configuracion", u"Lineas", None))
        self.push_Menu.setText("")
        self.label.setText(QCoreApplication.translate("Configuracion", u"-", None))
        self.push_Desactivar.setText(QCoreApplication.translate("Configuracion", u"Desactivar", None))
        self.radioButton_2.setText(QCoreApplication.translate("Configuracion", u"Tipo", None))
        self.push_Activar.setText(QCoreApplication.translate("Configuracion", u"Activar", None))
    # retranslateUi

