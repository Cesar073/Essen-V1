# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VtnaProm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VtnaCombos(object):
    def setupUi(self, VtnaCombos):
        if not VtnaCombos.objectName():
            VtnaCombos.setObjectName(u"VtnaCombos")
        VtnaCombos.resize(1366, 700)
        self.groupBox_4 = QGroupBox(VtnaCombos)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(630, 550, 231, 141))
        font = QFont()
        font.setPointSize(16)
        self.groupBox_4.setFont(font)
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 60, 101, 31))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label_4.setFont(font1)
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 100, 101, 31))
        self.label_8.setFont(font1)
        self.line_PorcRegalo = QLineEdit(self.groupBox_4)
        self.line_PorcRegalo.setObjectName(u"line_PorcRegalo")
        self.line_PorcRegalo.setGeometry(QRect(120, 60, 101, 31))
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(12)
        self.line_PorcRegalo.setFont(font2)
        self.line_PorcRegalo.setAlignment(Qt.AlignCenter)
        self.line_MargenRegalo = QLineEdit(self.groupBox_4)
        self.line_MargenRegalo.setObjectName(u"line_MargenRegalo")
        self.line_MargenRegalo.setGeometry(QRect(120, 100, 101, 31))
        self.line_MargenRegalo.setFont(font2)
        self.line_MargenRegalo.setAlignment(Qt.AlignCenter)
        self.push_Sugerir = QPushButton(self.groupBox_4)
        self.push_Sugerir.setObjectName(u"push_Sugerir")
        self.push_Sugerir.setGeometry(QRect(10, 10, 211, 41))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(16)
        self.push_Sugerir.setFont(font3)
        self.push_Sugerir.setAutoDefault(False)
        self.groupBox_1 = QGroupBox(VtnaCombos)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setGeometry(QRect(870, 0, 231, 111))
        self.groupBox_1.setFont(font)
        self.label_3 = QLabel(self.groupBox_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 40, 71, 21))
        self.label_3.setFont(font1)
        self.label_5 = QLabel(self.groupBox_1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 80, 101, 21))
        self.label_5.setFont(font1)
        self.label_GPorc = QLabel(self.groupBox_1)
        self.label_GPorc.setObjectName(u"label_GPorc")
        self.label_GPorc.setGeometry(QRect(120, 70, 101, 31))
        self.label_GPorc.setFont(font1)
        self.label_GPorc.setStyleSheet(u"border: 1px solid black;\n"
"color: rgb(255, 0, 0);\n"
"border-color: rgb(216, 216, 216);")
        self.label_GPorc.setAlignment(Qt.AlignCenter)
        self.label_GPesos = QLabel(self.groupBox_1)
        self.label_GPesos.setObjectName(u"label_GPesos")
        self.label_GPesos.setGeometry(QRect(120, 30, 101, 31))
        self.label_GPesos.setFont(font1)
        self.label_GPesos.setStyleSheet(u"border: 1px solid black;\n"
"color: rgb(255, 0, 0);\n"
"border-color: rgb(216, 216, 216);")
        self.label_GPesos.setAlignment(Qt.AlignCenter)
        self.groupBox_3 = QGroupBox(VtnaCombos)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(870, 120, 481, 251))
        self.groupBox_3.setFont(font)
        self.list_Cuotas = QListWidget(self.groupBox_3)
        self.list_Cuotas.setObjectName(u"list_Cuotas")
        self.list_Cuotas.setGeometry(QRect(10, 40, 71, 201))
        font4 = QFont()
        font4.setPointSize(14)
        self.list_Cuotas.setFont(font4)
        self.list_Interes = QListWidget(self.groupBox_3)
        self.list_Interes.setObjectName(u"list_Interes")
        self.list_Interes.setGeometry(QRect(80, 40, 81, 201))
        self.list_Interes.setFont(font4)
        self.list_Pcio_Ctas = QListWidget(self.groupBox_3)
        self.list_Pcio_Ctas.setObjectName(u"list_Pcio_Ctas")
        self.list_Pcio_Ctas.setGeometry(QRect(160, 40, 131, 201))
        self.list_Pcio_Ctas.setFont(font4)
        self.list_Pcio_Ctas.setAutoScroll(False)
        self.push_Int1 = QPushButton(self.groupBox_3)
        self.push_Int1.setObjectName(u"push_Int1")
        self.push_Int1.setGeometry(QRect(300, 40, 171, 41))
        self.push_Int1.setFont(font4)
        self.push_Int1.setAutoDefault(False)
        self.push_Int2 = QPushButton(self.groupBox_3)
        self.push_Int2.setObjectName(u"push_Int2")
        self.push_Int2.setGeometry(QRect(300, 80, 171, 41))
        self.push_Int2.setFont(font4)
        self.push_Int2.setAutoDefault(False)
        self.push_Int3 = QPushButton(self.groupBox_3)
        self.push_Int3.setObjectName(u"push_Int3")
        self.push_Int3.setGeometry(QRect(300, 120, 171, 41))
        self.push_Int3.setFont(font4)
        self.push_Int3.setAutoDefault(False)
        self.push_Int4 = QPushButton(self.groupBox_3)
        self.push_Int4.setObjectName(u"push_Int4")
        self.push_Int4.setGeometry(QRect(300, 160, 171, 41))
        self.push_Int4.setFont(font4)
        self.push_Int4.setAutoDefault(False)
        self.push_Int5 = QPushButton(self.groupBox_3)
        self.push_Int5.setObjectName(u"push_Int5")
        self.push_Int5.setGeometry(QRect(300, 200, 171, 41))
        self.push_Int5.setFont(font4)
        self.push_Int5.setAutoDefault(False)
        self.label_24 = QLabel(self.groupBox_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(300, 10, 171, 31))
        self.label_24.setFont(font1)
        self.label_24.setAlignment(Qt.AlignCenter)
        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(80, 10, 81, 31))
        self.label_22.setFont(font1)
        self.label_22.setAlignment(Qt.AlignCenter)
        self.label_23 = QLabel(self.groupBox_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(160, 10, 131, 31))
        self.label_23.setFont(font1)
        self.label_23.setAlignment(Qt.AlignCenter)
        self.label_21 = QLabel(self.groupBox_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 10, 81, 31))
        self.label_21.setFont(font1)
        self.label_21.setAlignment(Qt.AlignCenter)
        self.list_Cuotas.raise_()
        self.list_Interes.raise_()
        self.list_Pcio_Ctas.raise_()
        self.push_Int2.raise_()
        self.push_Int3.raise_()
        self.push_Int4.raise_()
        self.push_Int5.raise_()
        self.push_Int1.raise_()
        self.label_24.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_21.raise_()
        self.groupBox_2 = QGroupBox(VtnaCombos)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(1110, 0, 231, 111))
        self.groupBox_2.setFont(font)
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 40, 71, 21))
        self.label_7.setFont(font1)
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 80, 101, 21))
        self.label_9.setFont(font1)
        self.label_GDPorc = QLabel(self.groupBox_2)
        self.label_GDPorc.setObjectName(u"label_GDPorc")
        self.label_GDPorc.setGeometry(QRect(120, 70, 101, 31))
        self.label_GDPorc.setFont(font1)
        self.label_GDPorc.setStyleSheet(u"border: 1px solid black;\n"
"color: rgb(255, 0, 0);\n"
"border-color: rgb(216, 216, 216);")
        self.label_GDPorc.setAlignment(Qt.AlignCenter)
        self.label_GDPesos = QLabel(self.groupBox_2)
        self.label_GDPesos.setObjectName(u"label_GDPesos")
        self.label_GDPesos.setGeometry(QRect(120, 30, 101, 31))
        self.label_GDPesos.setFont(font1)
        self.label_GDPesos.setStyleSheet(u"border: 1px solid black;\n"
"color: rgb(255, 0, 0);\n"
"border-color: rgb(216, 216, 216);")
        self.label_GDPesos.setAlignment(Qt.AlignCenter)
        self.push_Bproduc = QPushButton(VtnaCombos)
        self.push_Bproduc.setObjectName(u"push_Bproduc")
        self.push_Bproduc.setGeometry(QRect(10, 30, 131, 71))
        self.push_Bproduc.setFont(font1)
        icon = QIcon()
        icon.addFile(u"icon/buscarlupa.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Bproduc.setIcon(icon)
        self.push_Bproduc.setIconSize(QSize(48, 48))
        self.push_Bproduc.setAutoDefault(False)
        self.push_Menu = QPushButton(VtnaCombos)
        self.push_Menu.setObjectName(u"push_Menu")
        self.push_Menu.setGeometry(QRect(1200, 619, 160, 71))
        font5 = QFont()
        font5.setFamily(u"Arial Black")
        font5.setPointSize(16)
        font5.setBold(True)
        font5.setItalic(True)
        font5.setWeight(75)
        self.push_Menu.setFont(font5)
        icon1 = QIcon()
        icon1.addFile(u"icon/home.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Menu.setIcon(icon1)
        self.push_Menu.setIconSize(QSize(60, 60))
        self.push_Menu.setAutoDefault(False)
        self.push_Guardar_Imagen = QPushButton(VtnaCombos)
        self.push_Guardar_Imagen.setObjectName(u"push_Guardar_Imagen")
        self.push_Guardar_Imagen.setGeometry(QRect(1200, 549, 160, 71))
        self.push_Guardar_Imagen.setFont(font5)
        icon2 = QIcon()
        icon2.addFile(u"icon/guardararchivo.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Guardar_Imagen.setIcon(icon2)
        self.push_Guardar_Imagen.setIconSize(QSize(60, 60))
        self.push_Guardar_Imagen.setAutoDefault(False)
        self.groupBox_5 = QGroupBox(VtnaCombos)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(150, 10, 471, 91))
        font6 = QFont()
        font6.setFamily(u"MS Shell Dlg 2")
        font6.setPointSize(16)
        font6.setBold(False)
        font6.setWeight(50)
        self.groupBox_5.setFont(font6)
        self.combo_Tipo_Imagen = QComboBox(self.groupBox_5)
        self.combo_Tipo_Imagen.setObjectName(u"combo_Tipo_Imagen")
        self.combo_Tipo_Imagen.setGeometry(QRect(10, 40, 241, 41))
        font7 = QFont()
        font7.setFamily(u"MS Shell Dlg 2")
        font7.setPointSize(14)
        font7.setBold(False)
        font7.setWeight(50)
        self.combo_Tipo_Imagen.setFont(font7)
        self.label = QLabel(self.groupBox_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 20, 71, 21))
        self.label.setFont(font7)
        self.label.setAlignment(Qt.AlignCenter)
        self.line_Numero = QLineEdit(self.groupBox_5)
        self.line_Numero.setObjectName(u"line_Numero")
        self.line_Numero.setGeometry(QRect(260, 40, 71, 41))
        self.line_Numero.setFont(font7)
        self.line_Numero.setAlignment(Qt.AlignCenter)
        self.push_Resta1 = QPushButton(self.groupBox_5)
        self.push_Resta1.setObjectName(u"push_Resta1")
        self.push_Resta1.setGeometry(QRect(340, 40, 61, 41))
        self.push_Resta1.setFont(font7)
        self.push_Resta1.setIconSize(QSize(48, 48))
        self.push_Resta1.setAutoDefault(False)
        self.push_Suma1 = QPushButton(self.groupBox_5)
        self.push_Suma1.setObjectName(u"push_Suma1")
        self.push_Suma1.setGeometry(QRect(400, 40, 61, 41))
        self.push_Suma1.setFont(font7)
        self.push_Suma1.setIcon(icon)
        self.push_Suma1.setIconSize(QSize(48, 48))
        self.push_Suma1.setAutoDefault(False)
        self.push_Activado = QPushButton(VtnaCombos)
        self.push_Activado.setObjectName(u"push_Activado")
        self.push_Activado.setGeometry(QRect(10, 550, 221, 51))
        self.push_Activado.setFont(font4)
        self.push_Activado.setAutoDefault(False)
        self.push_ListaCombo = QPushButton(VtnaCombos)
        self.push_ListaCombo.setObjectName(u"push_ListaCombo")
        self.push_ListaCombo.setGeometry(QRect(10, 610, 221, 51))
        self.push_ListaCombo.setFont(font4)
        self.push_ListaCombo.setAutoDefault(False)
        self.groupBox_6 = QGroupBox(VtnaCombos)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 110, 851, 431))
        self.push_Limpiar = QPushButton(self.groupBox_6)
        self.push_Limpiar.setObjectName(u"push_Limpiar")
        self.push_Limpiar.setGeometry(QRect(120, 370, 111, 51))
        self.push_Limpiar.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u"icon/limpiararchivo2.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Limpiar.setIcon(icon3)
        self.push_Limpiar.setIconSize(QSize(40, 40))
        self.push_Limpiar.setAutoDefault(False)
        self.label_17 = QLabel(self.groupBox_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(280, 400, 161, 20))
        self.label_17.setFont(font1)
        self.label_15 = QLabel(self.groupBox_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(280, 370, 111, 20))
        self.label_15.setFont(font1)
        self.push_Borrar = QPushButton(self.groupBox_6)
        self.push_Borrar.setObjectName(u"push_Borrar")
        self.push_Borrar.setGeometry(QRect(10, 370, 111, 51))
        self.push_Borrar.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u"icon/goma.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Borrar.setIcon(icon4)
        self.push_Borrar.setIconSize(QSize(40, 40))
        self.push_Borrar.setAutoDefault(False)
        self.list_Pspv = QListWidget(self.groupBox_6)
        self.list_Pspv.setObjectName(u"list_Pspv")
        self.list_Pspv.setGeometry(QRect(640, 90, 101, 281))
        font8 = QFont()
        font8.setFamily(u"Calibri")
        font8.setPointSize(14)
        self.list_Pspv.setFont(font8)
        self.list_Pspv.setLayoutDirection(Qt.RightToLeft)
        self.list_Desc = QListWidget(self.groupBox_6)
        self.list_Desc.setObjectName(u"list_Desc")
        self.list_Desc.setGeometry(QRect(390, 90, 51, 281))
        self.list_Desc.setFont(font8)
        self.list_Desc.setLayoutDirection(Qt.RightToLeft)
        self.label_14 = QLabel(self.groupBox_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(740, 70, 101, 20))
        font9 = QFont()
        font9.setFamily(u"Candara")
        font9.setPointSize(14)
        font9.setBold(True)
        font9.setItalic(True)
        font9.setWeight(75)
        self.label_14.setFont(font9)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_TCosto = QLabel(self.groupBox_6)
        self.label_TCosto.setObjectName(u"label_TCosto")
        self.label_TCosto.setGeometry(QRect(440, 370, 101, 21))
        font10 = QFont()
        font10.setFamily(u"Calibri")
        font10.setPointSize(14)
        font10.setBold(True)
        font10.setWeight(75)
        self.label_TCosto.setFont(font10)
        self.label_TCosto.setStyleSheet(u"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"border-color: rgb(95, 95, 95);")
        self.label_TCosto.setAlignment(Qt.AlignCenter)
        self.push_Regalo = QPushButton(self.groupBox_6)
        self.push_Regalo.setObjectName(u"push_Regalo")
        self.push_Regalo.setGeometry(QRect(160, 10, 151, 51))
        self.push_Regalo.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u"icon/pngocean.com.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Regalo.setIcon(icon5)
        self.push_Regalo.setIconSize(QSize(50, 50))
        self.push_Regalo.setAutoDefault(False)
        self.label_12 = QLabel(self.groupBox_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(540, 70, 101, 20))
        self.label_12.setFont(font9)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.list_Detalle = QListWidget(self.groupBox_6)
        self.list_Detalle.setObjectName(u"list_Detalle")
        self.list_Detalle.setGeometry(QRect(10, 90, 381, 281))
        self.list_Detalle.setFont(font8)
        self.label_16 = QLabel(self.groupBox_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(390, 70, 51, 20))
        self.label_16.setFont(font9)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(self.groupBox_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(646, 70, 91, 20))
        self.label_13.setFont(font9)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.list_Lista = QListWidget(self.groupBox_6)
        self.list_Lista.setObjectName(u"list_Lista")
        self.list_Lista.setGeometry(QRect(740, 90, 101, 281))
        self.list_Lista.setFont(font8)
        self.list_Lista.setLayoutDirection(Qt.RightToLeft)
        self.list_Costo10 = QListWidget(self.groupBox_6)
        self.list_Costo10.setObjectName(u"list_Costo10")
        self.list_Costo10.setGeometry(QRect(540, 90, 101, 281))
        self.list_Costo10.setFont(font8)
        self.list_Costo10.setLayoutDirection(Qt.RightToLeft)
        self.label_DPspv = QLabel(self.groupBox_6)
        self.label_DPspv.setObjectName(u"label_DPspv")
        self.label_DPspv.setGeometry(QRect(640, 400, 101, 21))
        self.label_DPspv.setFont(font10)
        self.label_DPspv.setStyleSheet(u"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"border-color: rgb(95, 95, 95);")
        self.label_DPspv.setAlignment(Qt.AlignCenter)
        self.label_TCosto10 = QLabel(self.groupBox_6)
        self.label_TCosto10.setObjectName(u"label_TCosto10")
        self.label_TCosto10.setGeometry(QRect(540, 370, 101, 21))
        self.label_TCosto10.setFont(font10)
        self.label_TCosto10.setStyleSheet(u"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"border-color: rgb(95, 95, 95);")
        self.label_TCosto10.setAlignment(Qt.AlignCenter)
        self.label_TLista = QLabel(self.groupBox_6)
        self.label_TLista.setObjectName(u"label_TLista")
        self.label_TLista.setGeometry(QRect(740, 370, 101, 21))
        self.label_TLista.setFont(font10)
        self.label_TLista.setStyleSheet(u"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"border-color: rgb(95, 95, 95);")
        self.label_TLista.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.groupBox_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(14, 69, 391, 21))
        self.label_10.setFont(font9)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_TPspv = QLabel(self.groupBox_6)
        self.label_TPspv.setObjectName(u"label_TPspv")
        self.label_TPspv.setGeometry(QRect(640, 370, 101, 21))
        self.label_TPspv.setFont(font10)
        self.label_TPspv.setStyleSheet(u"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"border-color: rgb(95, 95, 95);")
        self.label_TPspv.setAlignment(Qt.AlignCenter)
        self.label_TDesc = QLabel(self.groupBox_6)
        self.label_TDesc.setObjectName(u"label_TDesc")
        self.label_TDesc.setGeometry(QRect(390, 370, 51, 21))
        self.label_TDesc.setFont(font10)
        self.label_TDesc.setStyleSheet(u"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"border-color: rgb(95, 95, 95);")
        self.label_TDesc.setAlignment(Qt.AlignCenter)
        self.push_Cprecio = QPushButton(self.groupBox_6)
        self.push_Cprecio.setObjectName(u"push_Cprecio")
        self.push_Cprecio.setGeometry(QRect(310, 10, 151, 51))
        self.push_Cprecio.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u"MainW/ui/icon/cambiar.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Cprecio.setIcon(icon6)
        self.push_Cprecio.setAutoDefault(False)
        self.list_Costo = QListWidget(self.groupBox_6)
        self.list_Costo.setObjectName(u"list_Costo")
        self.list_Costo.setGeometry(QRect(440, 90, 101, 281))
        self.list_Costo.setFont(font8)
        self.list_Costo.setLayoutDirection(Qt.RightToLeft)
        self.label_11 = QLabel(self.groupBox_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(440, 70, 101, 20))
        self.label_11.setFont(font9)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.push_Descuento = QPushButton(self.groupBox_6)
        self.push_Descuento.setObjectName(u"push_Descuento")
        self.push_Descuento.setGeometry(QRect(10, 10, 151, 51))
        self.push_Descuento.setFont(font1)
        icon7 = QIcon()
        icon7.addFile(u"icon/descuento2.png", QSize(), QIcon.Normal, QIcon.On)
        self.push_Descuento.setIcon(icon7)
        self.push_Descuento.setIconSize(QSize(30, 30))
        self.push_Descuento.setAutoDefault(False)
        self.label_DLista = QLabel(self.groupBox_6)
        self.label_DLista.setObjectName(u"label_DLista")
        self.label_DLista.setGeometry(QRect(740, 400, 101, 21))
        self.label_DLista.setFont(font10)
        self.label_DLista.setStyleSheet(u"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"border-color: rgb(95, 95, 95);")
        self.label_DLista.setAlignment(Qt.AlignCenter)
        self.groupBox_7 = QGroupBox(VtnaCombos)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(630, 20, 231, 80))
        self.label_Fecha_Act = QLabel(self.groupBox_7)
        self.label_Fecha_Act.setObjectName(u"label_Fecha_Act")
        self.label_Fecha_Act.setGeometry(QRect(0, 40, 231, 31))
        self.label_Fecha_Act.setFont(font)
        self.label_Fecha_Act.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.groupBox_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 231, 31))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.push_Crear_Imagen = QPushButton(VtnaCombos)
        self.push_Crear_Imagen.setObjectName(u"push_Crear_Imagen")
        self.push_Crear_Imagen.setGeometry(QRect(1200, 410, 160, 71))
        self.push_Crear_Imagen.setFont(font5)
        self.push_Crear_Imagen.setIcon(icon2)
        self.push_Crear_Imagen.setIconSize(QSize(60, 60))
        self.push_Crear_Imagen.setAutoDefault(False)
        self.label_Msj = QLabel(VtnaCombos)
        self.label_Msj.setObjectName(u"label_Msj")
        self.label_Msj.setGeometry(QRect(10, 670, 611, 21))
        font11 = QFont()
        font11.setFamily(u"Mongolian Baiti")
        font11.setPointSize(14)
        font11.setBold(False)
        font11.setItalic(False)
        font11.setWeight(50)
        self.label_Msj.setFont(font11)
        self.label_Msj.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.push_Editar_Imagen = QPushButton(VtnaCombos)
        self.push_Editar_Imagen.setObjectName(u"push_Editar_Imagen")
        self.push_Editar_Imagen.setGeometry(QRect(1200, 480, 160, 71))
        self.push_Editar_Imagen.setFont(font5)
        self.push_Editar_Imagen.setIcon(icon2)
        self.push_Editar_Imagen.setIconSize(QSize(60, 60))
        self.push_Editar_Imagen.setAutoDefault(False)
        self.label_Imagen = QLabel(VtnaCombos)
        self.label_Imagen.setObjectName(u"label_Imagen")
        self.label_Imagen.setGeometry(QRect(870, 390, 321, 301))

        self.retranslateUi(VtnaCombos)

        QMetaObject.connectSlotsByName(VtnaCombos)
    # setupUi

    def retranslateUi(self, VtnaCombos):
        VtnaCombos.setWindowTitle(QCoreApplication.translate("VtnaCombos", u"Dialog", None))
        self.groupBox_4.setTitle("")
        self.label_4.setText(QCoreApplication.translate("VtnaCombos", u"Porcentaje", None))
        self.label_8.setText(QCoreApplication.translate("VtnaCombos", u"Margen", None))
        self.push_Sugerir.setText(QCoreApplication.translate("VtnaCombos", u"Sugerir regalo", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("VtnaCombos", u"Ganancia", None))
        self.label_3.setText(QCoreApplication.translate("VtnaCombos", u"Pesos", None))
        self.label_5.setText(QCoreApplication.translate("VtnaCombos", u"Porcentaje", None))
        self.label_GPorc.setText("")
        self.label_GPesos.setText("")
        self.groupBox_3.setTitle("")
#if QT_CONFIG(tooltip)
        self.list_Interes.setToolTip(QCoreApplication.translate("VtnaCombos", u"<html><head/><body><p>Doble clic y editamos su inter\u00e9s (Ajusta el Precio autom\u00e1ticamente)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.list_Pcio_Ctas.setToolTip(QCoreApplication.translate("VtnaCombos", u"<html><head/><body><p>Doble clic y editamos el precio (Ajusta el inter\u00e9s autom\u00e1ticamente)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.push_Int1.setText(QCoreApplication.translate("VtnaCombos", u"Intereses 1", None))
        self.push_Int2.setText(QCoreApplication.translate("VtnaCombos", u"Intereses 2", None))
        self.push_Int3.setText(QCoreApplication.translate("VtnaCombos", u"Intereses 3", None))
        self.push_Int4.setText(QCoreApplication.translate("VtnaCombos", u"Intereses 4", None))
        self.push_Int5.setText(QCoreApplication.translate("VtnaCombos", u"Intereses 5", None))
        self.label_24.setText(QCoreApplication.translate("VtnaCombos", u"Listas de Intereses", None))
        self.label_22.setText(QCoreApplication.translate("VtnaCombos", u"Inter\u00e9s", None))
        self.label_23.setText(QCoreApplication.translate("VtnaCombos", u"Precio", None))
        self.label_21.setText(QCoreApplication.translate("VtnaCombos", u"Cuotas", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("VtnaCombos", u"Gcia c/ Descuento", None))
        self.label_7.setText(QCoreApplication.translate("VtnaCombos", u"Pesos", None))
        self.label_9.setText(QCoreApplication.translate("VtnaCombos", u"Porcentaje", None))
        self.label_GDPorc.setText("")
        self.label_GDPesos.setText("")
#if QT_CONFIG(tooltip)
        self.push_Bproduc.setToolTip(QCoreApplication.translate("VtnaCombos", u"<html><head/><body><p align=\"center\">Buscar<br/>Producto</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.push_Bproduc.setWhatsThis(QCoreApplication.translate("VtnaCombos", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.push_Bproduc.setText(QCoreApplication.translate("VtnaCombos", u"Producto", None))
        self.push_Menu.setText("")
        self.push_Guardar_Imagen.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("VtnaCombos", u"Buscar Combo", None))
        self.label.setText(QCoreApplication.translate("VtnaCombos", u"N\u00famero", None))
        self.line_Numero.setText("")
        self.push_Resta1.setText(QCoreApplication.translate("VtnaCombos", u"<", None))
        self.push_Suma1.setText(QCoreApplication.translate("VtnaCombos", u">", None))
        self.push_Activado.setText(QCoreApplication.translate("VtnaCombos", u"Activado", None))
        self.push_ListaCombo.setText(QCoreApplication.translate("VtnaCombos", u"Lista Combos", None))
        self.groupBox_6.setTitle("")
        self.push_Limpiar.setText(QCoreApplication.translate("VtnaCombos", u"Limpiar", None))
        self.label_17.setText(QCoreApplication.translate("VtnaCombos", u"TOTAL APL. DESC", None))
        self.label_15.setText(QCoreApplication.translate("VtnaCombos", u"TOTAL REAL", None))
        self.push_Borrar.setText(QCoreApplication.translate("VtnaCombos", u"Borrar", None))
        self.label_14.setText(QCoreApplication.translate("VtnaCombos", u"P. LISTA", None))
        self.label_TCosto.setText("")
        self.push_Regalo.setText(QCoreApplication.translate("VtnaCombos", u"Regalo", None))
        self.label_12.setText(QCoreApplication.translate("VtnaCombos", u"PC + 10%", None))
        self.label_16.setText(QCoreApplication.translate("VtnaCombos", u"DESC", None))
        self.label_13.setText(QCoreApplication.translate("VtnaCombos", u"PSPV", None))
        self.label_DPspv.setText("")
        self.label_TCosto10.setText("")
        self.label_TLista.setText("")
        self.label_10.setText(QCoreApplication.translate("VtnaCombos", u"DETALLE", None))
        self.label_TPspv.setText("")
        self.label_TDesc.setText("")
        self.push_Cprecio.setText(QCoreApplication.translate("VtnaCombos", u"Cambiar Precio", None))
        self.label_11.setText(QCoreApplication.translate("VtnaCombos", u"P. COSTO", None))
        self.push_Descuento.setText(QCoreApplication.translate("VtnaCombos", u"Descuento", None))
        self.label_DLista.setText("")
        self.groupBox_7.setTitle("")
        self.label_Fecha_Act.setText(QCoreApplication.translate("VtnaCombos", u"-", None))
        self.label_2.setText(QCoreApplication.translate("VtnaCombos", u"Actualizado al:", None))
        self.push_Crear_Imagen.setText(QCoreApplication.translate("VtnaCombos", u"Crear Imagen", None))
        self.label_Msj.setText(QCoreApplication.translate("VtnaCombos", u"Listas de Intereses", None))
        self.push_Editar_Imagen.setText("")
        self.label_Imagen.setText(QCoreApplication.translate("VtnaCombos", u"TextLabel", None))
    # retranslateUi
