# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VtnaStockinter.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Stockinterno(object):
    def setupUi(self, Stockinterno):
        if not Stockinterno.objectName():
            Stockinterno.setObjectName(u"Stockinterno")
        Stockinterno.resize(1366, 700)
        self.label = QLabel(Stockinterno)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 110, 47, 13))
        font = QFont()
        font.setFamily(u"Candara")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.push_Menu = QPushButton(Stockinterno)
        self.push_Menu.setObjectName(u"push_Menu")
        self.push_Menu.setGeometry(QRect(1060, 500, 160, 80))
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
        self.label_4 = QLabel(Stockinterno)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(720, 110, 41, 21))
        self.label_4.setFont(font)
        self.label_6 = QLabel(Stockinterno)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(890, 80, 51, 52))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFont(font)
        self.label_6.setLineWidth(0)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setIndent(-1)
        self.listView_6 = QListView(Stockinterno)
        self.listView_6.setObjectName(u"listView_6")
        self.listView_6.setGeometry(QRect(880, 130, 81, 311))
        self.label_2 = QLabel(Stockinterno)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 110, 47, 13))
        self.label_2.setFont(font)
        self.listView = QListView(Stockinterno)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(110, 130, 51, 311))
        self.listView_2 = QListView(Stockinterno)
        self.listView_2.setObjectName(u"listView_2")
        self.listView_2.setGeometry(QRect(700, 130, 81, 311))
        self.listView_3 = QListView(Stockinterno)
        self.listView_3.setObjectName(u"listView_3")
        self.listView_3.setGeometry(QRect(170, 130, 251, 311))
        self.label_3 = QLabel(Stockinterno)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(476, 110, 161, 20))
        self.label_3.setFont(font)
        self.label_5 = QLabel(Stockinterno)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(790, 80, 81, 51))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.listView_4 = QListView(Stockinterno)
        self.listView_4.setObjectName(u"listView_4")
        self.listView_4.setGeometry(QRect(430, 130, 256, 311))
        self.listView_5 = QListView(Stockinterno)
        self.listView_5.setObjectName(u"listView_5")
        self.listView_5.setGeometry(QRect(790, 130, 81, 311))

        self.retranslateUi(Stockinterno)

        QMetaObject.connectSlotsByName(Stockinterno)
    # setupUi

    def retranslateUi(self, Stockinterno):
        Stockinterno.setWindowTitle(QCoreApplication.translate("Stockinterno", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Stockinterno", u"Cant.", None))
        self.push_Menu.setText("")
        self.label_4.setText(QCoreApplication.translate("Stockinterno", u"Costo", None))
        self.label_6.setText(QCoreApplication.translate("Stockinterno", u"<html><head/><body><p align=\"center\">Costo a</p><p align=\"center\">la fecha</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Stockinterno", u"Detalle", None))
        self.label_3.setText(QCoreApplication.translate("Stockinterno", u"Donde est\u00e1 fisicamente", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("Stockinterno", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Stockinterno", u"<html><head/><body><p align=\"center\">$ al d\u00eda</p><p align=\"center\">de la compra</p></body></html>", None))
    # retranslateUi

