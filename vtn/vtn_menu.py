# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VtnaMenu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1401, 723)
        icon = QIcon()
        icon.addFile(u"icon/inicio.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.push_Producto = QPushButton(self.centralwidget)
        self.push_Producto.setObjectName(u"push_Producto")
        self.push_Producto.setGeometry(QRect(130, 30, 261, 201))
        icon1 = QIcon()
        icon1.addFile(u"icon/cocina3.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Producto.setIcon(icon1)
        self.push_Producto.setIconSize(QSize(200, 200))
        self.push_Ofertas = QPushButton(self.centralwidget)
        self.push_Ofertas.setObjectName(u"push_Ofertas")
        self.push_Ofertas.setGeometry(QRect(390, 30, 261, 201))
        icon2 = QIcon()
        icon2.addFile(u"icon/promo.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Ofertas.setIcon(icon2)
        self.push_Ofertas.setIconSize(QSize(150, 150))
        self.push_Pedidos = QPushButton(self.centralwidget)
        self.push_Pedidos.setObjectName(u"push_Pedidos")
        self.push_Pedidos.setGeometry(QRect(650, 30, 261, 201))
        icon3 = QIcon()
        icon3.addFile(u"icon/productos2.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Pedidos.setIcon(icon3)
        self.push_Pedidos.setIconSize(QSize(200, 150))
        self.push_Clientes = QPushButton(self.centralwidget)
        self.push_Clientes.setObjectName(u"push_Clientes")
        self.push_Clientes.setGeometry(QRect(130, 270, 261, 201))
        icon4 = QIcon()
        icon4.addFile(u"icon/clientes2.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Clientes.setIcon(icon4)
        self.push_Clientes.setIconSize(QSize(200, 150))
        self.push_Stock = QPushButton(self.centralwidget)
        self.push_Stock.setObjectName(u"push_Stock")
        self.push_Stock.setGeometry(QRect(390, 270, 261, 201))
        icon5 = QIcon()
        icon5.addFile(u"icon/stock.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Stock.setIcon(icon5)
        self.push_Stock.setIconSize(QSize(200, 200))
        self.push_Recordatorio = QPushButton(self.centralwidget)
        self.push_Recordatorio.setObjectName(u"push_Recordatorio")
        self.push_Recordatorio.setGeometry(QRect(650, 270, 261, 201))
        icon6 = QIcon()
        icon6.addFile(u"icon/recordatorio.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Recordatorio.setIcon(icon6)
        self.push_Recordatorio.setIconSize(QSize(200, 150))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 230, 171, 20))
        self.label.setStyleSheet(u"color: rgb(255, 170, 0);\n"
"font: 87 16pt \"Arial Black\";")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(410, 230, 241, 20))
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 170, 0);\n"
"font: 87 12pt \"Arial Black\";")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 470, 131, 20))
        self.label_4.setStyleSheet(u"color: rgb(255, 170, 0);\n"
"font: 87 16pt \"Arial Black\";")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(410, 470, 211, 20))
        self.label_5.setStyleSheet(u"color: rgb(255, 170, 0);\n"
"font: 87 16pt \"Arial Black\";")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(680, 470, 201, 20))
        self.label_6.setStyleSheet(u"color: rgb(255, 170, 0);\n"
"font: 87 16pt \"Arial Black\";")
        self.push_Estado = QPushButton(self.centralwidget)
        self.push_Estado.setObjectName(u"push_Estado")
        self.push_Estado.setGeometry(QRect(910, 270, 261, 201))
        icon7 = QIcon()
        icon7.addFile(u"icon/ventas.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Estado.setIcon(icon7)
        self.push_Estado.setIconSize(QSize(200, 150))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(910, 470, 261, 20))
        self.label_8.setStyleSheet(u"color: rgb(255, 170, 0);\n"
"font: 87 16pt \"Arial Black\";")
        self.push_Ventas = QPushButton(self.centralwidget)
        self.push_Ventas.setObjectName(u"push_Ventas")
        self.push_Ventas.setGeometry(QRect(910, 30, 261, 201))
        icon8 = QIcon()
        icon8.addFile(u"icon/ventas2.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Ventas.setIcon(icon8)
        self.push_Ventas.setIconSize(QSize(200, 120))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(980, 230, 101, 20))
        self.label_9.setStyleSheet(u"color: rgb(255, 170, 0);\n"
"font: 87 16pt \"Arial Black\";")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(720, 230, 111, 20))
        self.label_10.setStyleSheet(u"color: rgb(255, 170, 0);\n"
"font: 87 16pt \"Arial Black\";")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(980, 660, 191, 20))
        self.label_11.setStyleSheet(u"color: rgb(255, 170, 0);\n"
"font: 87 14pt \"Arial Black\";")
        self.push_Configuracion = QPushButton(self.centralwidget)
        self.push_Configuracion.setObjectName(u"push_Configuracion")
        self.push_Configuracion.setGeometry(QRect(980, 510, 191, 151))
        icon9 = QIcon()
        icon9.addFile(u"icon/configuracion.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Configuracion.setIcon(icon9)
        self.push_Configuracion.setIconSize(QSize(150, 130))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Men\u00fa", None))
        self.push_Producto.setText("")
        self.push_Ofertas.setText("")
        self.push_Pedidos.setText("")
        self.push_Clientes.setText("")
        self.push_Stock.setText("")
        self.push_Recordatorio.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"PRODUCTOS", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"OFERTAS / CREAR PROMO", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CLIENTES", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"STOCK INTERNO", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"RECORDATORIOS", None))
        self.push_Estado.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ESTADO PATRIMONIAL", None))
        self.push_Ventas.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"VENTAS", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"PEDIDOS", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"CONFIGURACI\u00d3N", None))
        self.push_Configuracion.setText("")
    # retranslateUi

