# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VtnaImagenes.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1366, 700)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 171, 581))
        font = QFont()
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 110, 151, 81))
        self.pushButton_2.setAutoDefault(False)
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 30, 151, 81))
        self.pushButton.setAutoDefault(False)
        self.pushButton_8 = QPushButton(self.groupBox)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(10, 190, 151, 81))
        self.pushButton_8.setAutoDefault(False)
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(190, 10, 171, 581))
        self.groupBox_2.setFont(font)
        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 110, 151, 81))
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 30, 151, 81))
        self.pushButton_4.setAutoDefault(False)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(760, 10, 600, 600))
        self.label.setStyleSheet(u"background: white;\n"
"border: 1px solid rgb(0,0,255);\n"
"")
        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(370, 10, 171, 581))
        self.groupBox_3.setFont(font)
        self.pushButton_5 = QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 110, 151, 81))
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_6 = QPushButton(self.groupBox_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(10, 30, 151, 81))
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_7 = QPushButton(self.groupBox_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(10, 190, 151, 81))
        self.pushButton_7.setAutoDefault(False)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Tipo de Imagen", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Individuales", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Combos", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"Sorteos", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Tama\u00f1o", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"600 x 600\n"
"Instagram", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"600 x 400\n"
"Wsp, Face, etc", None))
        self.label.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Tama\u00f1o", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Productos", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"Fondo", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"Ubicaci\u00f3n\n"
"Precios", None))
    # retranslateUi

