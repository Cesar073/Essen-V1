# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VtnaClieNuevo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ClienteNuevo(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1366, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.push_Anterior = QPushButton(self.centralwidget)
        self.push_Anterior.setObjectName(u"push_Anterior")
        self.push_Anterior.setGeometry(QRect(1200, 610, 160, 80))
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.push_Anterior.setFont(font)
        icon = QIcon()
        icon.addFile(u"././icon/anterior.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Anterior.setIcon(icon)
        self.push_Anterior.setIconSize(QSize(60, 60))
        self.push_Anterior.setAutoDefault(False)
        self.push_Elimina_Item = QPushButton(self.centralwidget)
        self.push_Elimina_Item.setObjectName(u"push_Elimina_Item")
        self.push_Elimina_Item.setGeometry(QRect(960, 550, 401, 41))
        self.push_Elimina_Item.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u"././icon/cancelar2.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Elimina_Item.setIcon(icon1)
        self.push_Elimina_Item.setIconSize(QSize(35, 35))
        self.push_Elimina_Item.setAutoDefault(False)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 451, 571))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.groupBox.setFont(font1)
        self.line_6 = QLineEdit(self.groupBox)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(150, 330, 61, 31))
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.line_6.setFont(font2)
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 240, 131, 20))
        font3 = QFont()
        font3.setFamily(u"Javanese Text")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.label_10.setFont(font3)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 140, 131, 21))
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_23 = QLabel(self.groupBox)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(20, 390, 121, 20))
        self.label_23.setFont(font3)
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_22 = QLabel(self.groupBox)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 340, 131, 20))
        self.label_22.setFont(font3)
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line_0 = QLineEdit(self.groupBox)
        self.line_0.setObjectName(u"line_0")
        self.line_0.setGeometry(QRect(150, 30, 291, 31))
        self.line_0.setFont(font2)
        self.Label_2 = QLabel(self.groupBox)
        self.Label_2.setObjectName(u"Label_2")
        self.Label_2.setGeometry(QRect(20, 90, 121, 21))
        self.Label_2.setFont(font3)
        self.Label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line_5 = QLineEdit(self.groupBox)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(150, 280, 291, 31))
        self.line_5.setFont(font2)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 40, 131, 21))
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 190, 131, 21))
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line_2 = QLineEdit(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(150, 130, 291, 31))
        self.line_2.setFont(font2)
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 290, 121, 20))
        self.label_11.setFont(font3)
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line_3 = QLineEdit(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(150, 180, 291, 31))
        self.line_3.setFont(font2)
        self.line_4 = QLineEdit(self.groupBox)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(150, 230, 291, 31))
        self.line_4.setFont(font2)
        self.line_1 = QLineEdit(self.groupBox)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setGeometry(QRect(150, 80, 291, 31))
        self.line_1.setFont(font2)
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(150, 380, 291, 181))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setItalic(False)
        self.textEdit.setFont(font4)
        self.push_Limpiar = QPushButton(self.centralwidget)
        self.push_Limpiar.setObjectName(u"push_Limpiar")
        self.push_Limpiar.setGeometry(QRect(10, 610, 160, 80))
        self.push_Limpiar.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u"././icon/limpiararchivo2.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Limpiar.setIcon(icon2)
        self.push_Limpiar.setIconSize(QSize(60, 60))
        self.push_Limpiar.setAutoDefault(False)
        self.push_Agrega_Deseo = QPushButton(self.centralwidget)
        self.push_Agrega_Deseo.setObjectName(u"push_Agrega_Deseo")
        self.push_Agrega_Deseo.setGeometry(QRect(960, 330, 201, 41))
        font5 = QFont()
        font5.setFamily(u"Arial Black")
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setItalic(True)
        font5.setWeight(75)
        self.push_Agrega_Deseo.setFont(font5)
        icon3 = QIcon()
        icon3.addFile(u"././icon/check.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Agrega_Deseo.setIcon(icon3)
        self.push_Agrega_Deseo.setIconSize(QSize(35, 35))
        self.push_Agrega_Deseo.setAutoDefault(False)
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(470, 10, 481, 671))
        self.groupBox_3.setFont(font1)
        self.combo_Conocimiento = QComboBox(self.groupBox_3)
        self.combo_Conocimiento.setObjectName(u"combo_Conocimiento")
        self.combo_Conocimiento.setGeometry(QRect(150, 629, 321, 31))
        font6 = QFont()
        font6.setFamily(u"Calibri")
        font6.setPointSize(12)
        font6.setItalic(False)
        self.combo_Conocimiento.setFont(font6)
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 339, 131, 21))
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line_16 = QLineEdit(self.groupBox_3)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setGeometry(QRect(150, 479, 321, 31))
        self.line_16.setFont(font2)
        self.line_9 = QLineEdit(self.groupBox_3)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(150, 129, 321, 31))
        self.line_9.setFont(font2)
        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 89, 131, 21))
        self.label_12.setFont(font3)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line_11 = QLineEdit(self.groupBox_3)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(150, 229, 321, 31))
        self.line_11.setFont(font2)
        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 539, 131, 21))
        self.label_15.setFont(font3)
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 638, 131, 21))
        self.label_9.setFont(font3)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 139, 111, 21))
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line_17 = QLineEdit(self.groupBox_3)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setGeometry(QRect(150, 529, 321, 31))
        self.line_17.setFont(font2)
        self.line_13 = QLineEdit(self.groupBox_3)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setGeometry(QRect(150, 329, 321, 31))
        self.line_13.setFont(font2)
        self.Label_3 = QLabel(self.groupBox_3)
        self.Label_3.setObjectName(u"Label_3")
        self.Label_3.setGeometry(QRect(20, 289, 121, 21))
        self.Label_3.setFont(font3)
        self.Label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 389, 131, 21))
        self.label_7.setFont(font3)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 439, 131, 20))
        self.label_14.setFont(font3)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line_14 = QLineEdit(self.groupBox_3)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setGeometry(QRect(150, 379, 321, 31))
        self.line_14.setFont(font2)
        self.line_12 = QLineEdit(self.groupBox_3)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setGeometry(QRect(150, 279, 321, 31))
        self.line_12.setFont(font2)
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 238, 111, 21))
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 489, 121, 20))
        self.label_16.setFont(font3)
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line_8 = QLineEdit(self.groupBox_3)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(150, 79, 321, 31))
        self.line_8.setFont(font2)
        self.line_15 = QLineEdit(self.groupBox_3)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setGeometry(QRect(150, 429, 321, 31))
        self.line_15.setFont(font2)
        self.line_10 = QLineEdit(self.groupBox_3)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(150, 180, 321, 31))
        self.line_10.setFont(font2)
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 189, 111, 21))
        self.label_8.setFont(font3)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_26 = QLabel(self.groupBox_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 40, 131, 20))
        self.label_26.setFont(font3)
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line_7 = QLineEdit(self.groupBox_3)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(150, 29, 321, 31))
        self.line_7.setFont(font2)
        self.line_18 = QLineEdit(self.groupBox_3)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setGeometry(QRect(150, 579, 321, 31))
        self.line_18.setFont(font2)
        self.label_27 = QLabel(self.groupBox_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 589, 131, 21))
        self.label_27.setFont(font3)
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.push_Guardar = QPushButton(self.centralwidget)
        self.push_Guardar.setObjectName(u"push_Guardar")
        self.push_Guardar.setGeometry(QRect(1040, 610, 160, 80))
        self.push_Guardar.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u"././icon/guardararchivo.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Guardar.setIcon(icon4)
        self.push_Guardar.setIconSize(QSize(60, 60))
        self.push_Guardar.setAutoDefault(False)
        self.push_Agrega_Record = QPushButton(self.centralwidget)
        self.push_Agrega_Record.setObjectName(u"push_Agrega_Record")
        self.push_Agrega_Record.setGeometry(QRect(1160, 330, 201, 41))
        self.push_Agrega_Record.setFont(font5)
        icon5 = QIcon()
        icon5.addFile(u"././icon/recordatorio.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Agrega_Record.setIcon(icon5)
        self.push_Agrega_Record.setIconSize(QSize(35, 35))
        self.push_Agrega_Record.setAutoDefault(False)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(960, 10, 401, 271))
        self.groupBox_2.setFont(font1)
        self.combo_MetP5 = QComboBox(self.groupBox_2)
        self.combo_MetP5.setObjectName(u"combo_MetP5")
        self.combo_MetP5.setGeometry(QRect(100, 230, 291, 31))
        self.combo_MetP5.setFont(font6)
        self.label_21 = QLabel(self.groupBox_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 240, 91, 21))
        self.label_21.setFont(font3)
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.combo_MetP3 = QComboBox(self.groupBox_2)
        self.combo_MetP3.setObjectName(u"combo_MetP3")
        self.combo_MetP3.setGeometry(QRect(100, 130, 291, 31))
        self.combo_MetP3.setFont(font6)
        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 140, 91, 21))
        self.label_18.setFont(font3)
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.combo_MetP1 = QComboBox(self.groupBox_2)
        self.combo_MetP1.setObjectName(u"combo_MetP1")
        self.combo_MetP1.setGeometry(QRect(100, 30, 291, 31))
        self.combo_MetP1.setFont(font6)
        self.combo_MetP2 = QComboBox(self.groupBox_2)
        self.combo_MetP2.setObjectName(u"combo_MetP2")
        self.combo_MetP2.setGeometry(QRect(100, 80, 291, 31))
        self.combo_MetP2.setFont(font6)
        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(0, 90, 91, 20))
        self.label_19.setFont(font3)
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.combo_MetP4 = QComboBox(self.groupBox_2)
        self.combo_MetP4.setObjectName(u"combo_MetP4")
        self.combo_MetP4.setGeometry(QRect(100, 180, 291, 31))
        self.combo_MetP4.setFont(font6)
        self.label_20 = QLabel(self.groupBox_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(0, 190, 91, 21))
        self.label_20.setFont(font3)
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 40, 81, 20))
        self.label_17.setFont(font3)
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.list_Deseos = QListWidget(self.centralwidget)
        self.list_Deseos.setObjectName(u"list_Deseos")
        self.list_Deseos.setGeometry(QRect(960, 370, 401, 181))
        font7 = QFont()
        font7.setPointSize(12)
        self.list_Deseos.setFont(font7)
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.line_0, self.line_1)
        QWidget.setTabOrder(self.line_1, self.line_2)
        QWidget.setTabOrder(self.line_2, self.line_3)
        QWidget.setTabOrder(self.line_3, self.line_4)
        QWidget.setTabOrder(self.line_4, self.line_5)
        QWidget.setTabOrder(self.line_5, self.line_6)
        QWidget.setTabOrder(self.line_6, self.textEdit)
        QWidget.setTabOrder(self.textEdit, self.push_Limpiar)
        QWidget.setTabOrder(self.push_Limpiar, self.line_7)
        QWidget.setTabOrder(self.line_7, self.line_8)
        QWidget.setTabOrder(self.line_8, self.line_9)
        QWidget.setTabOrder(self.line_9, self.line_10)
        QWidget.setTabOrder(self.line_10, self.line_11)
        QWidget.setTabOrder(self.line_11, self.line_12)
        QWidget.setTabOrder(self.line_12, self.line_13)
        QWidget.setTabOrder(self.line_13, self.line_14)
        QWidget.setTabOrder(self.line_14, self.line_15)
        QWidget.setTabOrder(self.line_15, self.line_16)
        QWidget.setTabOrder(self.line_16, self.line_17)
        QWidget.setTabOrder(self.line_17, self.line_18)
        QWidget.setTabOrder(self.line_18, self.combo_Conocimiento)
        QWidget.setTabOrder(self.combo_Conocimiento, self.combo_MetP1)
        QWidget.setTabOrder(self.combo_MetP1, self.combo_MetP2)
        QWidget.setTabOrder(self.combo_MetP2, self.combo_MetP3)
        QWidget.setTabOrder(self.combo_MetP3, self.combo_MetP4)
        QWidget.setTabOrder(self.combo_MetP4, self.combo_MetP5)
        QWidget.setTabOrder(self.combo_MetP5, self.push_Agrega_Deseo)
        QWidget.setTabOrder(self.push_Agrega_Deseo, self.push_Agrega_Record)
        QWidget.setTabOrder(self.push_Agrega_Record, self.list_Deseos)
        QWidget.setTabOrder(self.list_Deseos, self.push_Elimina_Item)
        QWidget.setTabOrder(self.push_Elimina_Item, self.push_Guardar)
        QWidget.setTabOrder(self.push_Guardar, self.push_Anterior)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.push_Anterior.setText("")
        self.push_Elimina_Item.setText(QCoreApplication.translate("MainWindow", u"ELIMINA ITEM", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Datos Personales", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Nombre 3", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nombre 1", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Comentario", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Clasificaci\u00f3n", None))
        self.Label_2.setText(QCoreApplication.translate("MainWindow", u"Apellido 2", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Apellido 1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nombre 2", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Dni", None))
        self.push_Limpiar.setText("")
        self.push_Agrega_Deseo.setText(QCoreApplication.translate("MainWindow", u"DESEOS", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Contacto", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Instagram", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono Fijo", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Contacto 2", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Conocimiento", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Celular", None))
        self.Label_3.setText(QCoreApplication.translate("MainWindow", u"Facebook", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"email 1", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"email 2", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Contacto 1", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Localidad", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Agendado Cel", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Contacto 3", None))
        self.push_Guardar.setText("")
        self.push_Agrega_Record.setText(QCoreApplication.translate("MainWindow", u"RECORDATORIOS", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Formas de pago", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Opci\u00f3n 5", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Opci\u00f3n 3", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Opci\u00f3n 2", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Opci\u00f3n 4", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Opci\u00f3n 1", None))
    # retranslateUi

