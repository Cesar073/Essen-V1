from PySide2.QtWidgets import QMainWindow, QInputDialog, QMessageBox
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QPixmap, QIcon

#import random
from PySide2.QtGui import *

from vtn.vtn_cli_nue import Ui_ClienteNuevo
from vtn.cla_busc import V_Buscar

import mod.vars as mi_vars
import mod.mdb as mdb
import mod.form as fm


class V_ClienteNuevo(QMainWindow):
    def __init__(self, Vnt_Anterior, Buscado = ""):
        super(V_ClienteNuevo, self).__init__()
        # Acabo de borrar el "self" de la línea de abajo, para poner éste recordatorio.
            # Necesito adaptar la creación de un nuevo cliente, con la nueva tabla ChatsWsp que tiene la db
        self.ui = Ui_ClienteNuevo()
        self.ui.setupUi(self)
        self.Cli_buscado = 0
        self.Ant = Vnt_Anterior

        self.ui.line_5.textChanged.connect(self.Cambio_Line5)
        self.ui.line_6.textChanged.connect(self.Cambio_Line6)

        self.ui.push_Agrega_Record.clicked.connect(self.Btn_Recordatorio)
        self.ui.push_Elimina_Item.clicked.connect(self.Btn_Elimina_Item)
        self.ui.push_Limpiar.clicked.connect(self.Btn_Limpiar)
        self.ui.push_Guardar.clicked.connect(self.Btn_Guardar)

        # Se guardan los ID de los productos deseados por el cliente
        self.ListaDeseos = []
        # Se guarda el recordatorio
        self.ListaRecordatorios = []

    '''########################################################################################################################################
    ###########################################################################################################################################
                                                        FUNCIONES DE VENTANA                                                                '''

    def Carga_Cli_Buscado(self):
        if self.Cli_buscado != 0:
            # Datos Personales
            Reg = mdb.Reg_Un_param_Int(mi_vars.DB_CLIENTES, "DatosPersonales", "ID", self.Cli_buscado)
            for i in Reg:
                self.ui.line_0.setText(i[1])
                self.ui.line_1.setText(i[2])
                self.ui.line_2.setText(i[3])
                self.ui.line_3.setText(i[4])
                self.ui.line_4.setText(i[5])
                self.ui.line_5.setText(i[6])
                self.ui.line_6.setText(str(i[7]))
                self.ui.textEdit.setPlainText(i[8])
            # Datos del contacto
            Reg = mdb.Reg_Un_param_Int(mi_vars.DB_CLIENTES, "Contacto", "ID", self.Cli_buscado)
            for i in Reg:
                self.ui.line_7.setText(i[1])
                self.ui.line_8.setText(i[2])
                self.ui.line_9.setText(i[3])
                self.ui.line_10.setText(i[4])
                self.ui.line_11.setText(i[5])
                self.ui.line_12.setText(i[6])
                self.ui.line_13.setText(i[7])
                self.ui.line_14.setText(i[8])
                self.ui.line_15.setText(i[9])
                self.ui.line_16.setText(i[10])
                self.ui.line_17.setText(i[11])
                self.ui.line_18.setText(i[12])
                self.ui.combo_Conocimiento.setCurrentIndex(mdb.Dev_Dato_Int(mi_vars.DB_CLIENTES, "ConfigConocimiento", "ID", i[13], 1))
            # Formas de Pago
            ListaAux = []
            Reg = mdb.Reg_Un_param_Int(mi_vars.DB_CLIENTES, "FormasDePago", "ID", self.Cli_buscado)
            for i in Reg:
                ListaAux.append(i[1])
                ListaAux.append(i[2])
                ListaAux.append(i[3])
                ListaAux.append(i[4])
                ListaAux.append(i[5])
            ListaAux2 = []
            for i in ListaAux:
                if i == 0:
                    ListaAux2.append(0)
                else:
                    Reg = mdb.Reg_Un_param_Int(mi_vars.DB_CLIENTES, "ConfigFormaPago", "ID", i)
                    for pos in Reg:
                        ListaAux2.append(pos[1])
            self.ui.combo_MetP1.setCurrentIndex(ListaAux2[0])
            self.ui.combo_MetP2.setCurrentIndex(ListaAux2[1])
            self.ui.combo_MetP3.setCurrentIndex(ListaAux2[2])
            self.ui.combo_MetP4.setCurrentIndex(ListaAux2[3])
            self.ui.combo_MetP5.setCurrentIndex(ListaAux2[4])
            # Deseos
            self.ListaDeseos = []
            Reg = mdb.Reg_Un_param_Int(mi_vars.DB_CLIENTES, "SusProductos", "ID", self.Cli_buscado)
            produc = ""
            recFecha = ""
            recMensa = ""
            for pos in Reg:
                produc = pos[3]
                recFecha = pos[4]
                recMensa = pos[5]
            if produc != "":
                aux = ""
                for c in produc:
                    if c == "-":
                        self.ListaDeseos.append(int(aux))
                        aux = ""
                    else:
                        aux += c
            # Recordatorios
            self.ListaRecordatorios = []
            if len(recMensa) > 0:
                ListaF = []
                ListaM = []
                for i in range(1,100):
                    iniM = 0
                    finM = 0
                    iniF = 0
                    aux = "**" + str(i) + "**"
                    largo = len(aux)
                    # try para detectar si hay algún mensaje ennumerado, y tenemos un tope de 99 mensajes
                    try:
                        iniM = recMensa.index(aux) + largo
                    except:
                        # Con este break salimos de todo el bucle, debido a que no hay más mensajes.
                        break
                    # Determinamos el fin del mensaje
                    aux = "**" + str(i + 1) + "**"
                    try:
                        finM = recMensa.index(aux) + 1
                    except:
                        finM = len(recMensa)
                    # Agregamos el mensaje a la lista
                    ListaM.append(recMensa[iniM:finM])

                    # Si es que hay algún mensaje, ahora podemos ver si también hay fecha para dicho mensaje
                    aux = "(" + str(i) + ")"
                    largo = len(aux)
                    # try para detectar si hay alguna fecha ennumerada, y tenemos un tope de 99 fechas
                    try:
                        iniF = recFecha.index(aux)
                        # Sabiendo que las fechas se guardan en un formato exacto de 10 caracteres, con la info hasta el momento es suficiente para 
                        ListaF.append(recFecha[iniF + largo:iniF + largo + 10])
                    except:
                        ListaF.append(False)
                
                if len(ListaM) > 0:
                    for i in range(len(ListaM)):
                        msj = ""
                        if ListaF[i] != False:
                            msj = ListaF[i] + " - "
                        msj += ListaM[i]
                        self.ListaRecordatorios.append(msj)
            self.Carga_Listas()
        else:
            self.Limpia_Ventana()

    def showEvent(self, event):
        # Actualizamos los valores de los comboBox
        self.Actualiza_ComboBox()
        # Si se viene desde "Buscar Productos", entonces rellenamos la lista de Deseos
        if mi_vars.ORIGEN_BUSCAR == 1:
            mi_vars.ORIGEN_BUSCAR = 0
            if len(mi_vars.LISTABUSCADO) > 0:
                for id_ in mi_vars.LISTABUSCADO:
                    self.ListaDeseos.append(id_)
                mi_vars.LISTABUSCADO = []
                self.Carga_Listas()
        else:
            # Esta función se ejecuta sólo si hay un ID para un cliente
            self.Carga_Cli_Buscado()
        self.ui.line_0.setFocus()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.Ant.show()
    
    # Función que se ejecuta al iniciar la ventana que actualiza valores de combobox
    def Actualiza_ComboBox(self):
        # Actualizamos los valores de los combobox de formas de pago
        self.ui.combo_MetP1.clear()        
        self.ui.combo_MetP2.clear()
        self.ui.combo_MetP3.clear()
        self.ui.combo_MetP4.clear()
        self.ui.combo_MetP5.clear()
        Total = int(mdb.Dev_Total_Tabla_Clie("ConfigFormaPago"))
        self.ui.combo_MetP1.addItem("-")        
        self.ui.combo_MetP2.addItem("-")
        self.ui.combo_MetP3.addItem("-")
        self.ui.combo_MetP4.addItem("-")
        self.ui.combo_MetP5.addItem("-")
        for i in range(Total):
            Tabla = mdb.Dev_Tabla_Clie("ConfigFormaPago")
            for r in Tabla:
                if r[1] == i + 1:
                    texto = ""
                    if r[6] != "":
                        texto = r[6]
                    if r[7] != "":
                        texto += " - " + r[7]
                    if r[8] != "":
                        texto += " - " + r[8]
                    if r[9] != "":
                        texto += " - " + r[9]
                    self.ui.combo_MetP1.addItem(texto)        
                    self.ui.combo_MetP2.addItem(texto)
                    self.ui.combo_MetP3.addItem(texto)
                    self.ui.combo_MetP4.addItem(texto)
                    self.ui.combo_MetP5.addItem(texto)
        # Actualizamos el combobox de conocimiento
        Total = mdb.Dev_Total_Tabla_Clie("ConfigConocimiento")
        self.ui.combo_Conocimiento.addItem("-")
        for i in range(Total):
            Tabla = mdb.Dev_Tabla_Clie("ConfigConocimiento")
            for r in Tabla:
                if r[1] == i + 1:
                    self.ui.combo_Conocimiento.addItem(r[2])

    '''########################################################################################################################################
    ###########################################################################################################################################
                                                        FUNCIONES DE BOTONES                                                                '''
    
    def Cambio_Line5(self):
        self.ui.line_5.setText(fm.Devuelve_Entero(self.ui.line_5.text()))

    def Cambio_Line6(self):
        self.ui.line_6.setText(fm.Devuelve_Entero(self.ui.line_6.text()))

    def Btn_Recordatorio(self):
        Nro, ok = QInputDialog.getInt(self, "Seleccione con o sin Fecha", "1) Recordatorio CON fecha. \n2) Recordatorio SIN fecha.")
        if ok:
            if Nro == 1:
                Fecha, ok = QInputDialog.getText(self, "Ingrese Fecha", "La fecha debe contener el siguiente formato sin error: dd/mm/aaaa")
                if ok:
                    if len(Fecha) == 10:
                        if fm.Es_Fecha(Fecha):
                            Texto, ok = QInputDialog.getText(self, "Ingrese Recordatorio", "Ingrese el texto que desea agendar:")
                            self.ListaRecordatorios.append(Fecha + " - " + Texto)
                            self.Carga_Listas()
                    else:
                        QMessageBox.question(self, "Error", "Formato incorrecto.", QMessageBox.Ok)
                    
            elif Nro == 2:
                Texto, ok = QInputDialog.getText(self, "Ingrese Recordatorio", "Ingrese el texto que desea agendar:")
                if ok:
                    if len(Texto) > 0:
                        self.ListaRecordatorios.append(Texto)
                        self.Carga_Listas()
                    else:
                        QMessageBox.question(self, "Error", "No se puede cargar un recordatorio vacío.", QMessageBox.Ok)
            else:
                QMessageBox.question(self, "Error", "Debe ingresar los valores 1 o 2 únicamente.", QMessageBox.Ok)

    def Btn_Elimina_Item(self):
        pos = self.ui.list_Deseos.currentRow()
        largo = len(self.ListaDeseos)
        if pos < largo:
            self.ListaDeseos.pop(pos)
        else:
            self.ListaRecordatorios.pop(self.ui.list_Deseos.count() - 1 - largo)
        self.Carga_Listas()

    def Btn_Limpiar(self):
        self.Limpia_Ventana()

    def Btn_Buscar(self):
        texto, ok = QInputDialog.getText(self, "B", "Busc", QMessageBox.Ok | QMessageBox.Cancel)


    # Se agenda un nuevo cliente
    def Btn_Guardar(self):
        rta = QMessageBox.question(self, "ATENCIÓN!", "Controle bien los datos ya que el único dato que se exige es un APELLIDO para crear un registro.\n ¿Está seguro/a que desea guardar los cambios?", QMessageBox.Yes | QMessageBox.No)
        if rta == QMessageBox.Yes:
            Lista = []
            # Posiciones 0:7 >>> Datos personales
            Lista.append(self.ui.line_0.text())
            Lista.append(self.ui.line_1.text())
            Lista.append(self.ui.line_2.text())
            Lista.append(self.ui.line_3.text())
            Lista.append(self.ui.line_4.text())
            Lista.append(self.ui.line_5.text())
            if self.ui.line_6.text() != "":
                Lista.append(int(self.ui.line_6.text()))
            else:
                Lista.append(0)
            Lista.append(self.ui.textEdit.toPlainText())

            # Posiciones 8:12 >>> Formas de Pago
            if self.ui.combo_MetP1.currentIndex() > 0:
                Lista.append(mdb.Dev_Dato_Int(mi_vars.DB_CLIENTES, "ConfigFormaPago", "Orden", self.ui.combo_MetP1.currentIndex(),0))
            else:
                Lista.append(0)
            if self.ui.combo_MetP2.currentIndex() > 0:
                Lista.append(mdb.Dev_Dato_Int(mi_vars.DB_CLIENTES, "ConfigFormaPago", "Orden", self.ui.combo_MetP2.currentIndex(),0))
            else:
                Lista.append(0)
            if self.ui.combo_MetP3.currentIndex() > 0:
                Lista.append(mdb.Dev_Dato_Int(mi_vars.DB_CLIENTES, "ConfigFormaPago", "Orden", self.ui.combo_MetP3.currentIndex(),0))
            else:
                Lista.append(0)
            if self.ui.combo_MetP4.currentIndex() > 0:
                Lista.append(mdb.Dev_Dato_Int(mi_vars.DB_CLIENTES, "ConfigFormaPago", "Orden", self.ui.combo_MetP4.currentIndex(),0))
            else:
                Lista.append(0)
            if self.ui.combo_MetP5.currentIndex() > 0:
                Lista.append(mdb.Dev_Dato_Int(mi_vars.DB_CLIENTES, "ConfigFormaPago", "Orden", self.ui.combo_MetP5.currentIndex(),0))
            else:
                Lista.append(0)
            
            # Posiciones 13:17 >>> Sus productos
            # Pos: Adquirido
            Lista.append("")
            # Pos: En Proceso
            Lista.append("")
            # Pos: Deseos. El formato final queda del tipo string, pero son los ID de productos separados por guiones, ej: 35-66-
            aux = ""
            if len(self.ListaDeseos) > 0:
                for des in self.ListaDeseos:
                    aux += str(des) + "-"
                Lista.append(aux)
            else:
                Lista.append("")
            # Pos: Fecha y Recordatorios
            if len(self.ListaRecordatorios) > 0:
                Cont = 0
                AuxF = ""
                Record = ""
                for reg in self.ListaRecordatorios:
                    Cont += 1
                    if len(reg) > 9:
                        if fm.Es_Fecha(reg[0:10]):
                            AuxF += "(" + str(Cont) + ")" + reg[0:10]
                            Record += "**" + str(Cont) + "**" + reg[13:]
                        else:
                            Record += "**" + str(Cont) + "**" + reg
                    else:
                        Record += "**" + str(Cont) + "**" + reg
                if len(AuxF) > 0:
                    Lista.append(AuxF)
                else:
                    Lista.append("")
                Lista.append(Record)
            else:
                Lista.append("")
                Lista.append("")

            # Posiciones 18:28 >>> Contacto
            Lista.append(self.ui.line_7.text())
            Lista.append(self.ui.line_8.text())
            Lista.append(self.ui.line_9.text())
            Lista.append(self.ui.line_10.text())
            Lista.append(self.ui.line_11.text())
            Lista.append(self.ui.line_12.text())
            Lista.append(self.ui.line_13.text())
            Lista.append(self.ui.line_14.text())
            Lista.append(self.ui.line_15.text())
            Lista.append(self.ui.line_16.text())
            Lista.append(self.ui.line_17.text())
            Lista.append(self.ui.line_18.text())
            valor = self.ui.combo_Conocimiento.currentIndex()
            if valor > 0:
                Lista.append(mdb.Dev_ID_ClienteInt("ConfigConocimiento", "Orden", valor))
            else:
                Lista.append(0)

            if self.Cli_buscado > 0:
                mdb.Act_Cliente(self.Cli_buscado, Lista)
            else:
                # Creamos al cliente
                mdb.Add_Cliente_Nuevo(Lista)

            # Limpiamos la ventana para cargar un nuevo cliente
            self.Limpia_Ventana()

    def Btn_Anterior(self):
        self.close()

    '''########################################################################################################################################
    ###########################################################################################################################################
                                                        FUNCIONES GENERALES                                                                 '''

    # Limpia todos los datos de los lineEdit y el texto plano, y pone en cero los combobox
    def Limpia_Ventana(self):
        # Limpia todos los lineEdit
        for line in self.findChildren(QtWidgets.QLineEdit):
            line.clear()
        # Pone los ComboBox en 0
        for combo in self.findChildren(QtWidgets.QComboBox):
            combo.setCurrentIndex(0)
        # Listbox y textEdit
        self.ui.textEdit.clear()
        self.ui.list_Deseos.clear()
        # Limpia las variables que rellenan la lista
        self.ListaDeseos = []
        self.ListaRecordatorios = []
        self.Cli_buscado = 0

    # Llega una lista con Id's y la carga en el listwidget de deseos
    # Nota: siempre limpia toda la lista y vuelve a cargar primero los productos Deseados y luego los Recordatorios, es necesario éste orden para las eliminaciones de los items
    def Carga_Listas(self):
        self.ui.list_Deseos.clear()
        for Pos in self.ListaDeseos:
            Datos = mdb.Reg_Un_param(mi_vars.BaseDeDatos, "Productos", "ID", Pos)
            for Registro in Datos:
                # Piezas
                if Registro[3] > 0:
                    aux = mi_vars.LINEANUM.index(Registro[3])
                    self.ui.list_Deseos.addItem(mi_vars.LINEA[aux] + " " + mi_vars.TIPO[Registro[4]] + " " + mi_vars.INTERIOR[Registro[5]] + " " + Registro[11] + " cm " + Registro[12] + " Lts")
                else:
                    # Otros productos
                    Detalle = ''
                    if Registro[6] != "":
                        Detalle = Registro[6]
                    elif Registro[7] != "":
                        Detalle = Registro[7]
                    elif Registro[8] != "":
                        Detalle = Registro[8]
                    elif Registro[9] != "":
                        Detalle = Registro[9]
                    elif Registro[10] != "":
                        Detalle = Registro[10]
                    if Registro[11] != "":
                        Detalle += " " + Registro[11] + " cm "
                    if Registro[12] != "":
                        Detalle += " " + Registro[12] + " Lts"
                    self.ui.list_Deseos.addItem(Detalle)

        for rec in self.ListaRecordatorios:
            self.ui.list_Deseos.addItem(rec)

