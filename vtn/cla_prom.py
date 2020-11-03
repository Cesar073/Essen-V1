# * Botón de sugerir regalos
# * Que se vean los puntos que se generan con un combo

from PySide2.QtWidgets import QDialog, QMessageBox, QFileDialog, QInputDialog
from PySide2 import QtCore, QtGui, QtWidgets

from os import walk
import os
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtCore import QDir

import mod.form as fts
import mod.mdb as mdb
import mod.vars as mi_vars

from vtn.vtn_prom import Ui_VtnaCombos
from vtn.cla_busc import V_Buscar

class V_Promos(QDialog):
    def __init__(self, VentanaAnterior, Lista = []):
        super(V_Promos, self).__init__()
        self.ui = Ui_VtnaCombos()
        self.ui.setupUi(self)
        self.Ant = VentanaAnterior

        self.ui.line_Numero.textChanged.connect(self.Change_Line_Combos)

        #self.ui.push_Bproduc.clicked.connect(self.Abrimos_Vtna_Buscar)
        self.ui.push_Descuento.clicked.connect(self.Aplicamos_Descuento)
        self.ui.push_Regalo.clicked.connect(self.Regalo_100_desc)
        self.ui.push_Borrar.clicked.connect(self.Borrar_Uno)
        self.ui.push_Limpiar.clicked.connect(self.Limpiar)

        self.ui.push_Int1.clicked.connect(self.Btn_Int1)
        self.ui.push_Int2.clicked.connect(self.Btn_Int2)
        self.ui.push_Int3.clicked.connect(self.Btn_Int3)
        self.ui.push_Int4.clicked.connect(self.Btn_Int4)
        self.ui.push_Int5.clicked.connect(self.Btn_Int5)

        self.ui.list_Detalle.clicked.connect(self.ClickLista1)
        self.ui.list_Desc.clicked.connect(self.ClickLista2)
        self.ui.list_Costo.clicked.connect(self.ClickLista3)
        self.ui.list_Costo10.clicked.connect(self.ClickLista4)
        self.ui.list_Pspv.clicked.connect(self.ClickLista5)
        self.ui.list_Lista.clicked.connect(self.ClickLista6)
        
        self.ui.list_Desc.itemDoubleClicked.connect(self.Doble_Clic_Descuento)

        self.ui.line_PorcRegalo.textChanged.connect(self.Cambio_Line_Porc_Regalo)
        self.ui.line_MargenRegalo.textChanged.connect(self.Cambio_Line_Marg_Regalo)

        self.ui.push_Menu.clicked.connect(lambda: self.close())

        # Variable que indica cuál de las 5 opciones de intereses que tenemos disponibles, está apretada
        # Su valor corresponde a la ubicación en la columna que tiene cada uno dentro de la base de datos, que indica si está activa o no
        self.Op_Interes = 0

        # Ejecución de funciones
        if len(Lista) > 0:
            self.Carga_Listas(Lista)
        
        self.LINE_BOOL = False
        Registro = mdb.Reg_Un_param(mi_vars.BaseDeDatos, "Config", "Tabla", "Regalo")
        for Dato in Registro:
            self.ui.line_PorcRegalo.setText(str(Dato[2]))
            self.ui.line_MargenRegalo.setText(str(Dato[3]))
        self.LINE_BOOL = True

        self.PASOS = 0
        self.ui.push_Guardar_Imagen.setEnabled(False)
        self.ui.push_Crear_Imagen.clicked.connect(self.Paso1)

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.Ant.show()

    def showEvent(self, event):
        self.Actualiza_Combo()
        if mi_vars.ORIGEN_BUSCAR == 1:
            mi_vars.ORIGEN_BUSCAR = 0
            if len(mi_vars.LISTABUSCADO) > 0:
                self.Carga_Listas(mi_vars.LISTABUSCADO)   

    '''########################################################################################################################################
    ###########################################################################################################################################
                                                                    BOTONES                                                                 '''
    
    # Change en Line de combos
    def Change_Line_Combos(self):
        texto = self.ui.line_Numero.text()
        if texto != "":
            Valor = int(self.ui.line_Numero.text())
            self.BuscaCombo(Valor)
        else:
            self.ui.label_Imagen.clear()
            self.ui.label_Imagen.setText("")
        
    # Botón de Buscar
    def Abrimos_Vtna_Buscar(self):
        
        self.hide()
        self.ui.V_Buscar.mostrar()
        '''
        mi_vars.ORIGEN_BUSCAR = 2
        try:
            self.ui.Ventana_Buscar.show()
        except:
            self.ui.Ventana_Buscar = V_Buscar(self)
            self.ui.Ventana_Buscar.show()
        
        self.hide()
        self.V_Buscar.mostrar()
        '''

    # Botón para aplicar descuentos
    def Aplicamos_Descuento(self):
        # Controlamos que haya algo seleccionado en la lista
        posicion = self.ui.list_Detalle.currentRow()
        if posicion >= 0:
            # Capturamos el valor ingresado y si apretó OK, sino ignoramos todo
            texto, ok = QInputDialog.getText(self, "Descuento", "Indique en porcentaje el descuento a aplciar:")
            if ok and texto != "":
                
                # Controlamos de manera sensilla si el valor es numérico
                if fts.Es_Numero_Int(texto):
                    texto = int(texto)
                    # Si se ingresó un valor superior a 0 y menor que 100 o = 100, es un valor correcto, de lo contrario no se aplica desc
                    if texto >= 0 and texto <= 100:
                        self.ui.list_Desc.takeItem(posicion)
                        self.ui.list_Desc.insertItem(posicion, str(texto))
                        self.ui.list_Desc.setCurrentRow(posicion)
                        self.Act_Val_Ventana()
                    else:
                        QMessageBox.question(self, "Aviso!", "Valor ingresado erróneo.", QMessageBox.Ok)
                else:
                    QMessageBox.question(self, "Aviso!", "Valor ingresado erróneo.", QMessageBox.Ok)
        else:
            QMessageBox.question(self, "Aviso!", "Debe seleccionar un producto de la lista para aplicar su descuento.", QMessageBox.Ok)

    # Botón para aplicar regalo
    def Regalo_100_desc(self):
        # Controlamos que haya algo seleccionado en la lista
        posicion = self.ui.list_Detalle.currentRow()
        if posicion >= 0:
            if self.ui.list_Desc.item(posicion).text() == "100":
                self.ui.list_Desc.takeItem(posicion)
                self.ui.list_Desc.insertItem(posicion, "0")
                self.ui.list_Desc.setCurrentRow(posicion)
            else:
                self.ui.list_Desc.takeItem(posicion)
                self.ui.list_Desc.insertItem(posicion, "100")
                self.ui.list_Desc.setCurrentRow(posicion)
            self.Act_Val_Ventana()
        else:
            QMessageBox.question(self, "Aviso!", "Debe seleccionar un producto de la lista para aplicar su descuento.", QMessageBox.Ok)

    # Botón de borrar un ítem
    def Borrar_Uno(self):
        posicion = self.ui.list_Detalle.currentRow()
        self.ui.list_Detalle.takeItem(posicion)
        self.ui.list_Desc.takeItem(posicion)
        self.ui.list_Costo.takeItem(posicion)
        self.ui.list_Costo10.takeItem(posicion)
        self.ui.list_Pspv.takeItem(posicion)
        self.ui.list_Lista.takeItem(posicion)
        self.Act_Val_Ventana()
    
    # Botón de limpiar todas las listas
    def Limpiar(self):
        self.ui.list_Detalle.clear()
        self.ui.list_Desc.clear()
        self.ui.list_Costo.clear()
        self.ui.list_Costo10.clear()
        self.ui.list_Pspv.clear()
        self.ui.list_Lista.clear()
        self.ui.label_Fecha_Act.setText("-")
        self.Act_Val_Ventana()

    # Hacer un Clic en las listas (es para que se seleccionen todas cuando se toca una y simule ser una única lista)
    def ClickLista1(self):
        pos = self.ui.list_Detalle.currentRow()
        self.Seleccionamos_Listas(pos)
    def ClickLista2(self):
        pos = self.ui.list_Desc.currentRow()
        self.Seleccionamos_Listas(pos)
    def ClickLista3(self):
        pos = self.ui.list_Costo.currentRow()
        self.Seleccionamos_Listas(pos)
    def ClickLista4(self):
        pos = self.ui.list_Costo10.currentRow()
        self.Seleccionamos_Listas(pos)
    def ClickLista5(self):
        pos = self.ui.list_Pspv.currentRow()
        self.Seleccionamos_Listas(pos)
    def ClickLista6(self):
        pos = self.ui.list_Lista.currentRow()
        self.Seleccionamos_Listas(pos)
    def Seleccionamos_Listas(self, pos):
        self.ui.list_Detalle.setCurrentRow(pos)
        self.ui.list_Desc.setCurrentRow(pos)
        self.ui.list_Costo.setCurrentRow(pos)
        self.ui.list_Costo10.setCurrentRow(pos)
        self.ui.list_Pspv.setCurrentRow(pos)
        self.ui.list_Lista.setCurrentRow(pos)

    # Doble Clic en la lista de Descuento, es lo mismo que hacer clic en el push_Descuento
    def Doble_Clic_Descuento(self):
        self.Aplicamos_Descuento()

    def Cambio_Line_Porc_Regalo(self):
        if self.LINE_BOOL == True:
            self.ui.line_PorcRegalo.setText(fts.Devuelve_Entero(self.ui.line_PorcRegalo.text()))
            aux = 0
            if self.ui.line_PorcRegalo.text() != "":
                aux = int(self.ui.line_PorcRegalo.text())
            mdb.Act_Regalo_Porcentaje(aux)

    def Cambio_Line_Marg_Regalo(self):
        if self.LINE_BOOL == True:
            self.ui.line_MargenRegalo.setText(fts.Devuelve_Entero(self.ui.line_MargenRegalo.text()))
            aux = 0
            if self.ui.line_MargenRegalo.text() != "":
                aux = int(self.ui.line_MargenRegalo.text())
            mdb.Act_Regalo_Margen(aux)

    def Btn_Int1(self):
        Valor = 2
        if self.Boton_Presionado != Valor:
            self.ui.list_Cuotas.clear()
            self.ui.list_Interes.clear()
            self.ui.list_Pcio_Ctas.clear()
            Tabla = mdb.Dev_Tabla_Prod("Cuotas")
            btn = False
            for reg in Tabla:
                if reg[Valor] == 1:
                    btn = True
                    break
            if btn == True:
                self.Boton_Presionado(Valor)
                self.Act_Val_Ventana()
            else:
                self.Boton_Presionado(Valor)
                QMessageBox.question(self, "Aviso!", "No existen datos en éste tipo de interés. Continúe para agregar nuevos.", QMessageBox.Ok)
                for i in range(18):
                    self.ui.list_Cuotas.addItem(str(i + 1))
                    self.ui.list_Interes.addItem("0")
                    self.ui.list_Pcio_Ctas.addItem("0,00")
    def Btn_Int2(self):
        Valor = 4
        if self.Boton_Presionado != Valor:
            self.ui.list_Cuotas.clear()
            self.ui.list_Interes.clear()
            self.ui.list_Pcio_Ctas.clear()
            Tabla = mdb.Dev_Tabla_Prod("Cuotas")
            btn = False
            for reg in Tabla:
                if reg[Valor] == 1:
                    btn = True
                    break
            if btn == True:
                self.Boton_Presionado(Valor)
                self.Act_Val_Ventana()
            else:
                self.Boton_Presionado(Valor)
                QMessageBox.question(self, "Aviso!", "No existen datos en éste tipo de interés. Continúe para agregar nuevos.", QMessageBox.Ok)
                for i in range(18):
                    self.ui.list_Cuotas.addItem(str(i + 1))
                    self.ui.list_Interes.addItem("0")
                    self.ui.list_Pcio_Ctas.addItem("0,00")
    def Btn_Int3(self):
        Valor = 6
        if self.Boton_Presionado != Valor:
            self.ui.list_Cuotas.clear()
            self.ui.list_Interes.clear()
            self.ui.list_Pcio_Ctas.clear()
            Tabla = mdb.Dev_Tabla_Prod("Cuotas")
            btn = False
            for reg in Tabla:
                if reg[Valor] == 1:
                    btn = True
                    break
            if btn == True:
                self.Boton_Presionado(Valor)
                self.Act_Val_Ventana()
            else:
                self.Boton_Presionado(Valor)
                QMessageBox.question(self, "Aviso!", "No existen datos en éste tipo de interés. Continúe para agregar nuevos.", QMessageBox.Ok)
                for i in range(18):
                    self.ui.list_Cuotas.addItem(str(i + 1))
                    self.ui.list_Interes.addItem("0")
                    self.ui.list_Pcio_Ctas.addItem("0,00")
    def Btn_Int4(self):
        Valor = 8
        if self.Boton_Presionado != Valor:
            self.ui.list_Cuotas.clear()
            self.ui.list_Interes.clear()
            self.ui.list_Pcio_Ctas.clear()
            Tabla = mdb.Dev_Tabla_Prod("Cuotas")
            btn = False
            for reg in Tabla:
                if reg[Valor] == 1:
                    btn = True
                    break
            if btn == True:
                self.Boton_Presionado(Valor)
                self.Act_Val_Ventana()
            else:
                self.Boton_Presionado(Valor)
                QMessageBox.question(self, "Aviso!", "No existen datos en éste tipo de interés. Continúe para agregar nuevos.", QMessageBox.Ok)
                for i in range(18):
                    self.ui.list_Cuotas.addItem(str(i + 1))
                    self.ui.list_Interes.addItem("0")
                    self.ui.list_Pcio_Ctas.addItem("0,00")
    def Btn_Int5(self):
        Valor = 10
        if self.Boton_Presionado != Valor:
            self.ui.list_Cuotas.clear()
            self.ui.list_Interes.clear()
            self.ui.list_Pcio_Ctas.clear()
            Tabla = mdb.Dev_Tabla_Prod("Cuotas")
            btn = False
            for reg in Tabla:
                if reg[Valor] == 1:
                    btn = True
                    break
            if btn == True:
                self.Boton_Presionado(Valor)
                self.Act_Val_Ventana()
            else:
                self.Boton_Presionado(Valor)
                QMessageBox.question(self, "Aviso!", "No existen datos en éste tipo de interés. Continúe para agregar nuevos.", QMessageBox.Ok)
                for i in range(18):
                    self.ui.list_Cuotas.addItem(str(i + 1))
                    self.ui.list_Interes.addItem("0")
                    self.ui.list_Pcio_Ctas.addItem("0,00")

    # Rellenamos los valores del combobox
    def Actualiza_Combo(self):
        self.ui.combo_Tipo_Imagen.clear()
        for i in mi_vars.LISTA_TIPOS_IMAGENES:
            self.ui.combo_Tipo_Imagen.addItem(i)


    '''########################################################################################################################################
    ###########################################################################################################################################
                                                                    VENTANA                                                                 '''

    # Viene una lista de parámetro con valores de ID de productos y se cargan sus datos en las listas de la ventana. Sólo trabaja con los datos
        # de productos, es decir que si vamos a cargar una lista que corresponde a una promoción se hace en otra función.
    def Carga_Listas(self, Lista):
        for Pos in Lista:
            Datos = mdb.Reg_Un_param(mi_vars.BaseDeDatos, "Productos", "ID", Pos)
            for Registro in Datos:
                # Piezas
                if Registro[3] > 0:
                    aux = mi_vars.LINEANUM.index(Registro[3])
                    self.ui.list_Detalle.addItem(mi_vars.LINEA[aux] + " " + mi_vars.TIPO[Registro[4]] + " " + mi_vars.INTERIOR[Registro[5]] + " " + Registro[11] + " cm " + Registro[12] + " Lts")
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
                    self.ui.list_Detalle.addItem(Detalle)

                # Lista con los detalles
                self.ui.list_Desc.addItem("0")
                self.ui.list_Costo.addItem(fts.Formato_Decimal(Registro[13], 2))
                self.ui.list_Costo10.addItem(fts.Formato_Decimal(Registro[14], 2))
                self.ui.list_Pspv.addItem(fts.Formato_Decimal(Registro[15], 2))
                self.ui.list_Lista.addItem(fts.Formato_Decimal(Registro[16], 2))

                self.Act_Val_Ventana()

    # Ante cualquier cambio en la ventana, se actualizan todos los valores
    # Da por hecho que los datos en las listas están correctos, los utiliza para actualizar los demás datos de la ventana.
    def Act_Val_Ventana(self):

        # True: si hay datos en las listas - False: Cuando hay que poner todo en cero
        if self.ui.list_Detalle.count() > 0:

            TotalCosto = 0
            TotalPspv = 0
            TotalLista = 0

            # Total de la lista de precio de costo y su total si hay descuento
            acumula = 0.0
            descuento = 0.0
            conDesc = False
            for i in range(self.ui.list_Costo.count()):
                acumula += fts.Str_Float(self.ui.list_Costo.item(i).text())
            self.ui.label_TCosto.setText(fts.Formato_Decimal(acumula, 2))
            TotalCosto = acumula

            # Total de la lista de precio de costo + el 10% y su total si hay descuento
            acumula = 0.0
            descuento = 0.0
            conDesc = False
            for i in range(self.ui.list_Costo10.count()):
                acumula += fts.Str_Float(self.ui.list_Costo10.item(i).text())
            self.ui.label_TCosto10.setText(fts.Formato_Decimal(acumula, 2))

            # Total de la lista de PSPV y su total si hay descuento
            acumula = 0.0
            descuento = 0.0
            conDesc = False
            for i in range(self.ui.list_Pspv.count()):
                acumula += fts.Str_Float(self.ui.list_Pspv.item(i).text())
                valor = fts.Str_Float(self.ui.list_Desc.item(i).text())
                if valor > 0.0:
                    descuento += ((100.0 - valor) / 100) * fts.Str_Float(self.ui.list_Pspv.item(i).text())
                    conDesc = True
                else:
                    descuento += fts.Str_Float(self.ui.list_Pspv.item(i).text())
            self.ui.label_TPspv.setText(fts.Formato_Decimal(acumula, 2))
            if conDesc == True:
                self.ui.label_DPspv.setText(fts.Formato_Decimal(descuento, 2))
            TotalPspv = acumula

            # Total de la lista de precio de Lista y su total si hay descuento
            acumula = 0.0
            descuento = 0.0
            conDesc = False
            for i in range(self.ui.list_Lista.count()):
                acumula += fts.Str_Float(self.ui.list_Lista.item(i).text())
                valor = fts.Str_Float(self.ui.list_Desc.item(i).text())
                if valor > 0.0:
                    descuento += ((100.0 - valor) / 100) * fts.Str_Float(self.ui.list_Lista.item(i).text())
                    conDesc = True
                else:
                    descuento += fts.Str_Float(self.ui.list_Lista.item(i).text())
            self.ui.label_TLista.setText(fts.Formato_Decimal(acumula, 2))
            if conDesc == True:
                self.ui.label_DLista.setText(fts.Formato_Decimal(descuento, 2))
            TotalLista = acumula
        
            # Labels Ganancia
            self.ui.label_GPesos.setText(fts.Formato_Decimal(TotalPspv - TotalCosto, 2))
            self.ui.label_GPorc.setText(fts.Formato_Decimal(((TotalPspv - TotalCosto) * 100) / TotalPspv, 2))
            # Labels de Ganancia donde se ha aplicado el Descuento
            if conDesc == True:
                PspvDesc = fts.Str_Float(self.ui.label_DPspv.text())
                TotCosto = fts.Str_Float(self.ui.label_TCosto.text())
                self.ui.label_GDPesos.setText(fts.Formato_Decimal(PspvDesc - TotCosto, 2))
                self.ui.label_GDPorc.setText(fts.Formato_Decimal(((PspvDesc - TotCosto) * 100) / TotalPspv, 2))
            else:
                self.ui.label_GDPesos.setText('')
                self.ui.label_GDPorc.setText('')
            # Listas de las Cuotas
            self.ui.list_Cuotas.clear()
            self.ui.list_Interes.clear()
            self.ui.list_Pcio_Ctas.clear()
            if self.Op_Interes == 0:
                self.Op_Interes = 2
            Tabla = mdb.Dev_Tabla_Prod("Cuotas")
            if descuento > 0.0:
                aux2 = descuento
            else:
                aux2 = TotalLista
            for reg in Tabla:
                if reg[self.Op_Interes] == 1:
                    self.ui.list_Cuotas.addItem(str(reg[1]))
                    self.ui.list_Interes.addItem(fts.Formato_Decimal(reg[self.Op_Interes + 1], 2))
                    aux = (aux2 * (1 + (reg[self.Op_Interes + 1] / 100))) / reg[1]
                    self.ui.list_Pcio_Ctas.addItem(fts.Formato_Decimal(aux, 2))

            # Labels que indica el porcentaje real final de descuento que se está realizando
            if conDesc == True:
                self.ui.label_TDesc.setText(fts.Formato_Decimal((TotalPspv - PspvDesc) * 100 / TotalPspv, 2))
            else:
                self.ui.label_TDesc.setText('')
                self.ui.label_DPspv.setText('')
                self.ui.label_DLista.setText('')
        else:
            self.ui.label_TDesc.setText('')
            self.ui.label_TCosto.setText('')
            self.ui.label_TCosto10.setText('')
            self.ui.label_TPspv.setText('')
            self.ui.label_DPspv.setText('')
            self.ui.label_TLista.setText('')
            self.ui.label_DLista.setText('')

            self.ui.label_GPesos.setText('')
            self.ui.label_GPorc.setText('')
            self.ui.label_GDPesos.setText('')
            self.ui.label_GDPorc.setText('')

            self.ui.list_Cuotas.clear()
            self.ui.list_Interes.clear()
            self.ui.list_Pcio_Ctas.clear()
    
    # Presiona uno de los 5 botones de intereses
    def Boton_Presionado(self, Numero):
        self.ui.push_Int1.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.ui.push_Int2.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.ui.push_Int3.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.ui.push_Int4.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.ui.push_Int5.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.Op_Interes = Numero      
        if Numero == 2:
            self.ui.push_Int1.setStyleSheet("background-color: rgb(255, 170, 127);")
        elif Numero == 4:
            self.ui.push_Int2.setStyleSheet("background-color: rgb(255, 170, 127);")
        elif Numero == 6:
            self.ui.push_Int3.setStyleSheet("background-color: rgb(255, 170, 127);")
        elif Numero == 8:
            self.ui.push_Int4.setStyleSheet("background-color: rgb(255, 170, 127);")
        elif Numero == 10:
            self.ui.push_Int5.setStyleSheet("background-color: rgb(255, 170, 127);")

    # Busca un combo que viene por parámetro
    def BuscaCombo(self, Numero):
        try:
            imagen = "./com\\" + str(Numero) + ".jpg"
            self.Carga_Imagen(imagen)
        except:
            pass
        
        try:
            Lista = []
            Lista = mdb.Dev_Reg_Combo(Nro = Numero)
            ListaAux = []
            if Lista[0] != False:
                Cont = 0
                while Cont < 10:
                    if Lista[Cont + 5] != "":
                        ListaAux.append(Lista[Cont + 5])
                    else:
                        break
                self.Carga_Listas(ListaAux)

                Cont = 0
                while Cont < len(ListaAux):
                    self.ui.list_Desc.takeItem(Cont)
                    self.ui.list_Desc.insertItem(Cont, str(Lista[Cont + 15]))
        except:
            pass

    def Carga_Imagen(self, Ruta):
        Ancho = 301
        Alto = 311
        try:
            '''
            Imagen = QPixmap(Ruta)
            Imagen = Imagen.scaled(Ancho, Alto, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.ui.label_Imagen.setPixmap(Imagen)
            '''
            Imagen = QPixmap(Ruta)

            self.ui.label_Imagen.setPixmap(Imagen)
            self.ui.label_Imagen.setScaledContents(True)
            self.ui.label_Imagen.setText("")
        except:
            QMessageBox.question(self, "Error", "No se pudo cargar la imagen.", QMessageBox.Ok)
            self.ui.label_Imagen.clear()
            self.ui.label_Imagen.setText("Sin Imagen")

    '''########################################################################################################################################
    ###########################################################################################################################################
                                                            CREAR DATOS IMAGEN NUEVA                                                        '''

    # Paso 1
    # Prepara para cargar los productos
    def Paso1(self):
        # Controlamos si estabamos en cero, de lo contrario es porque se ha dejado sin terminar un paso y consultamos que se hace
        # Recordar que éste mismo botón inicia y cancela las cargas de imagenes
        if self.PASOS != 0:
            Rta = QMessageBox.question(self, "Atención!", "¿Desea CANCELAR la carga de la imagen actual?", QMessageBox.Yes | QMessageBox.No)
            if Rta == QMessageBox.No:
                return
        self.PASOS = 1
        self.Limpiar()
        self.ui.groupBox_1.setEnabled(False)
        self.ui.groupBox_2.setEnabled(False)
        self.ui.groupBox_3.setEnabled(False)
        self.ui.groupBox_4.setEnabled(False)
        self.ui.groupBox_5.setEnabled(False)
        self.ui.groupBox_6.setEnabled(False)
        self.ui.groupBox_7.setEnabled(False)
        self.ui.push_Bproduc.setEnabled(False)
        self.ui.push_Activado.setEnabled(False)
        self.ui.push_ListaCombo.setEnabled(False)
        self.ui.push_Crear_Imagen.setText("Cancelar")
        self.ui.label_Msj.setText("Paso 1 de 9. Elija la imagen a agregar.")
        self.ui.push_Imagen.setText("Seleccione Imagen")

        # Que seleccione una imagen
        Ruta = ""
        Ruta, _ = QFileDialog.getOpenFileName(self, 'Buscar Imagen',os.chdir("./Imagenes"), "All Files (*.jpg);;All Files (*.png)")
        
        # True: Operación normal. False: Ocurrió un error y no se ha podido encontrar la ruta
        if Ruta != "":
            self.Carga_Imagen(Ruta)
            
        else:
            QMessageBox.question(self, "Error", "No se ha seleccionado ningún archivo.", QMessageBox.Ok)
            self.Restaura()
            return
        self.Paso2()

    def Paso2(self):
        QMessageBox.question(self, "Paso 2", "A continuación seleccione los productos que tiene la imagen.", QMessageBox.Ok)
        self.ui.push_Bproduc.setEnabled(True)

    def Restaura(self):
        # Restaura lo del Paso 1
        self.PASOS = 0
        self.Limpiar()
        self.ui.groupBox_1.setEnabled(True)
        self.ui.groupBox_2.setEnabled(True)
        self.ui.groupBox_3.setEnabled(True)
        self.ui.groupBox_4.setEnabled(True)
        self.ui.groupBox_5.setEnabled(True)
        self.ui.groupBox_6.setEnabled(True)
        self.ui.groupBox_7.setEnabled(True)
        self.ui.push_Bproduc.setEnabled(True)
        self.ui.push_Activado.setEnabled(True)
        self.ui.push_ListaCombo.setEnabled(True)
        self.ui.push_Crear_Imagen.setText("Crear Imagen")
        self.ui.push_Guardar_Imagen.setEnabled(False)
        
        self.ui.label_Msj.setText("-")
        self.ui.push_Imagen.setText("Seleccione Imagen")


