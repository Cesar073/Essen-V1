''' ERRORES - PROYECTOS - NOTIFICACIONES - CAMBIOS
* Hay muchas variables que en su momento eran globales, por razones de practicidad y velocidad para la reimplementación de las mismas
        decidí hacerlas globales también, pero deberían ir en la clase con el prefijo self.
        Lo que sucede es que al menos en el archivo viejo habían casi 1500 líneas de código para ésta ventana, así que para recorrer todas
        las líneas y ajustar ésto demandaría muchísimo tiempo, por ende se implementan igual que allá, como variables globales.
* Cuando uso el excel para cargar datos nuevos, no está actualizando bien la fecha, tengo productos actualizados con un excel nuevo pero le figura que son del mes pasado



'''

from PySide2.QtWidgets import QDialog, QMessageBox, QFileDialog
# Módulos generales
import os
from os import walk
import sqlite3
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt, QDir
from PySide2.QtGui import QPixmap, QIcon
from datetime import datetime

from vtn.vtn_prod import Ui_Productos
from vtn.cla_busc import V_Buscar
import mod.mdb as mdb
import mod.form as fts
import mod.excel as exl
import mod.vars as mi_vars

AUTOM_ACT = 0

class V_Productos(QDialog):

    '''########################################################################################################################################
    ###########################################################################################################################################
                                                    FUNCIONES RELATIVAS A LA VENTANA                                                        '''
    def __init__(self, VentanaAnterior):
        super(V_Productos, self).__init__()
        self.ui = Ui_Productos()
        self.ui.setupUi(self)

        # VARIABLES
        # 01 - Ventana que se debe abrir al cerrar ésta
        self.Ant = VentanaAnterior
        # 02 - Total de Productos en la db
        self.TOTAL = 0
        # 03 - Total de Productos activos
        self.PROD_ACT = 0
        # 04 - Variables de apoyo para las funciones de Change_line_edit_ de valores en dinero
        self.LINEVALOR1 = ""
        self.LINEVALOR2 = ""
        self.LINEVALOR3 = ""
        self.LINEVALOR4 = ""
        # 05 - Indicadores si están activos o no los LineEdit para escribirlos sin que se ejecute el changeEvent
        self.LINE_ID_ACTIVO = True
        self.LINE_COD_ACTIVO = True
        self.LINE_PUNTOS_ACTIVO = True
        self.LINE_PUNTOSMG_ACTIVO = True
        
        # LES DAMOS VALOR A LAS VARIABLES
        # 02 - 03
        Datos = ['0']
        Filas = mdb.Dev_Reg_Prod_Config("Tabla", "Productos")
        for Fila in Filas:
            Datos[0] = Fila[2]
            Datos.append(Fila[3])
        if Datos[0] != "0":
            self.TOTAL = Datos[0]
            self.PROD_ACT = Datos[1]

        # LINE_EDIT
        # Identificación
        self.ui.line_ID.textChanged.connect(self.ChangeLineID)
        self.ui.line_Codigo.textChanged.connect(self.ChangeLineCodigo)
        # Concepto
        self.ui.line_Puntos.textChanged.connect(self.ChangeLinePuntos)
        self.ui.line_Puntos_MG.textChanged.connect(self.ChangeLinePuntosMG)
        # Costo
        self.ui.line_Pcio_Costo.keyPressEvent = self.keyPressEvent
        self.ui.line_Costo10.keyPressEvent = self.keyPressEvent
        self.ui.line_PSPV.keyPressEvent = self.keyPressEvent
        self.ui.line_Pcio_Lista.keyPressEvent = self.keyPressEvent

        # BOTONES
        #self.ui.push_Buscar.clicked.connect(self.Abrimos_Vtna_Buscar)
        self.ui.push_Anterior.clicked.connect(self.Clic_Anterior)
        self.ui.push_Siguiente.clicked.connect(self.Clic_Siguiente)
        self.ui.push_Guardar.clicked.connect(self.Clic_Guardar)
        self.ui.push_Limpiar.clicked.connect(self.LimpiarPantalla)
        self.ui.push_Excel.clicked.connect(self.Clic_RecorreExcel)
        self.ui.push_Menu.clicked.connect(self.CerrarProd)
    
    def mostrar(self):
        self.show()

    def showEvent(self, event):
        # Cargamos los valores de los comboBox
        self.ui.comboBox_Linea.clear()
        for i in mi_vars.LINEA:
            self.ui.comboBox_Linea.addItem(i)
        self.ui.comboBox_Tipo.clear()
        for i in mi_vars.TIPO:
            self.ui.comboBox_Tipo.addItem(i)
        self.ui.comboBox_Interior.clear()
        for i in mi_vars.INTERIOR:
            self.ui.comboBox_Interior.addItem(i)
        
        if mi_vars.ORIGEN_BUSCAR == 1:
            mi_vars.ORIGEN_BUSCAR = 0
            if len(mi_vars.LISTABUSCADO) > 0:
                self.ui.line_ID.setText(str(mi_vars.LISTABUSCADO[0]))
        
        self.ui.line_ID.setFocus()

    def closeEvent(self, event):
        # VARIABLES (Su detalle está en el INIT)
        if mi_vars.EXCEL == True:
            close = QMessageBox.question(self, "Salir", "Se está ejecutando la ACTUALIZACIÓN de la base de datos con el EXCEL, si sale de la ventana quedará incompleta la carga de productos. ¿Estás seguro/a que desea salir?", QMessageBox.Yes | QMessageBox.No)
            if close == QMessageBox.Yes:
                mi_vars.EXCEL = False
                mi_vars.Lineas = []
                mi_vars.Codigos = []
                mi_vars.Descripcion = []
                mi_vars.Pspv = []
                mi_vars.Precio = []
                mi_vars.Puntos = []
                mi_vars.PuntosMG = []
                mi_vars.Filas = []
                event.ignore()
                self.hide()
                self.Ant.show()
            else:
                event.ignore()
        else:
            event.ignore()
            self.hide()
            self.Ant.show()

    def CerrarProd(self):
        self.close()


    '''########################################################################################################################################
    ###########################################################################################################################################
                                                  FUNCIONES RELATIVAS A BOTONES EVENTOS                                                     '''

    def Abrimos_Vtna_Buscar(self): #***********
        mi_vars.Lineas = []
        mi_vars.Codigos = []
        mi_vars.Descripcion = []
        mi_vars.Pspv = []
        mi_vars.Precio = []
        mi_vars.Puntos = []
        mi_vars.PuntosMG = []
        mi_vars.Filas = []
        mi_vars.ORIGEN_BUSCAR = 3
        self.hide()
        try:
            self.ui.Ventana_Buscar.show()
        except:
            self.ui.Ventana_Buscar = V_Buscar(self)
            self.ui.Ventana_Buscar.show()

    def ChangeLineID(self): #***********
        # Si el ID está activado, se ejecuta su acción
        if self.LINE_ID_ACTIVO == True:
            
            # Si se limpió su ID entonces mandamos a limpiar toda la pantalla
            if self.ui.line_ID.text() == '':
                self.LimpiarPantalla(1)
            else:

                # Sólo permitimos números
                Actual = self.ui.line_ID.text()
                # En la variable Nuevo quedará en formato string sólo números, pero si no tenía valores posibles vuelve vacío
                Nuevo = fts.Devuelve_Entero(Actual)
                # True: Si lo ingresado está mal, queda todo como estaba. False: Si se ingresó un valor correcto, lo analizamos
                if Actual != Nuevo:
                    self.ui.line_ID.setText(Nuevo)
                
                else:
                    # Si lo que se digitó está correcto, entonces acá buscamos en la base de datos si el ID existe
                    ValorID = int(self.ui.line_ID.text())
                    if ValorID > 0:
                        if self.R_T_Busca_ID_Cod(True, ValorID) == True:
                            self.LINE_COD_ACTIVO = False
                            self.V_T_Cargar_Datos(self.R_T_Retorna_Datos_De_BBDD(ID=ValorID))
                            self.LINE_COD_ACTIVO = True
                        else:
                            self.LimpiarPantalla(1)

    def ChangeLineCodigo(self): #***********

        # Si el LINE_CODIGO está activo se ejecuta su acción
        if self.LINE_COD_ACTIVO == True:

            # Si se limpió su Codigo entonces mandamos a limpiar toda la pantalla
            if self.ui.line_Codigo.text() == '':
                self.LimpiarPantalla(2)
            else:

                # Sólo permitimos números
                Actual = self.ui.line_Codigo.text()
                # En la variable Nuevo quedará en formato string sólo números, pero si no tenía valores posibles vuelve vacío
                Nuevo = fts.Devuelve_Entero(Actual)
                # True: Si lo ingresado está mal, queda todo como estaba. False: Si se ingresó un valor correcto, lo analizamos
                if Actual != Nuevo:
                    self.ui.line_Codigo.setText(Nuevo)
                
                else:
                    # Si lo cargado es correcto, buscamos el producto
                    if self.R_T_Busca_ID_Cod(False, self.ui.line_Codigo.text()) == True:
                        self.LINE_ID_ACTIVO = False
                        self.V_T_Cargar_Datos(self.R_T_Retorna_Datos_De_BBDD(Codigo =self.ui.line_Codigo.text()))
                        self.LINE_ID_ACTIVO = True
                    else:
                        self.LimpiarPantalla(2)

    def ChangeLinePuntos(self): #***********
        if self.LINE_PUNTOS_ACTIVO == True:
            # Sólo permitimos números
            Actual = self.ui.line_Puntos.text()
            Nuevo = fts.Devuelve_Entero(Actual)
            if Actual != Nuevo:
                self.ui.line_Puntos.setText(Nuevo)

    def ChangeLinePuntosMG(self): #***********
        if self.LINE_PUNTOSMG_ACTIVO == True:
            # Sólo permitimos números
            Actual = self.ui.line_Puntos_MG.text()
            Nuevo = fts.Devuelve_Entero(Actual)
            if Actual != Nuevo:
                self.ui.line_Puntos_MG.setText(Nuevo)

    # Evento que guarda los cambios. A éste evento se lo puede llamar no sólo desde su botón sino también desde cualquier parte del programa.
        # 1- Verifica que se quiere hacer (guardar o crear)
        # 2- Prepara la info
        # 3- Controla y guarda

        # Nota: Si está activo la carga de archivos de Excel, luego de guardar ejecuta la función de self.Clic_Siguiente()
        # Siguiente3 >>> Cuando se ejecuta ésta función desde la función Clic_Siguiente(), no hay que volver a llamarla, por ende con ésta var lo arreglamos.
    def Clic_Guardar(self, Siguiente2 = False, Mensaje = True, Siguiente3 = True): #***********
        # PASO 1
        Respuesta = self.R_T_Verifica_Datos_Guardar_Crear(self.ui.line_ID.text(), self.ui.line_Codigo.text())        
        # PASO 2
        Datos = self.R_T_Convierte_Datos_Para_BD(self.R_T_Retorna_Datos_De_Ventana())
        # PASO 3
        if Respuesta == 1:
            if self.R_T_Control_Datos_Guardar(Datos, Mensaje) == 3:
                self.V_T_Guarda_Actualizacion(Datos)
                if mi_vars.EXCEL == True or Siguiente2 == True:
                    if Siguiente3 == True:
                        self.Clic_Siguiente(Controla=False)

        elif Respuesta == 2:
            if self.R_T_Control_Datos_Crear(Datos, Mensaje) == 3:
                self.V_T_Guarda_Producto_Nuevo(Datos)
                if mi_vars.EXCEL == True or Siguiente2 == True:
                    if Siguiente3 == True:
                        self.Clic_Siguiente(Controla=False)

    # Botón que funciona para retroceder tanto en la lista de productos de la bd como del excel.
    def Clic_Anterior(self): ###

        # Control: Si hubieron cambios y no se guardaron, aquí le avisamos al usuario y le permitimos guardarlo antes de continuar.
        self.V_C_Controla_Cambios_Guarda()

        # True: Cuando estamos actualizando con un excel
        if mi_vars.EXCEL == True:
            tope = len(mi_vars.Lineas) - 1
            mi_vars.CONTADOR_ -= 1
            if mi_vars.CONTADOR_ < 0:
                self.MuestraMsjOK("Se ha llegado al inicio de la lista, se mostrará el último producto en la posición: " + str(tope), "Fin de la lista")
                mi_vars.CONTADOR_ = tope
                self.Compara_Excel_BBDD()
            else:
                self.Compara_Excel_BBDD()
        
        # Operación normal
        else:
            
            # Retrocede una posición según la ubicación del registro actual, con respecto a la base de datos
            if self.ui.line_ID.text() != "":

                Valor = int(self.ui.line_ID.text())

                if Valor > 1:
                    self.ui.line_ID.setText(str(Valor-1))
                else:
                    # self.MuestraMsjOK("Los Registro de Productos son números enteros correlativos que comienzan desde el número 1, se cargará el último producto.", "Aviso")
                    self.ui.line_ID.setText(str(self.TOTAL))
            else:
                self.MuestraMsjOK("Debe haber un valor en el recuadro de ID", "Error al intentar retroceder un Registro")
                self.ui.line_ID.setFocus()

    # El valor Automático es para cuando el Excel está activado como automático. Esto quiere decir que todo control ya se ha realizado y sólo tenemos que continuar avanzando.
    def Clic_Siguiente(self, Automatico = False, Controla = True): ###

        # Control: Si hubieron cambios y no se guardaron, aquí le avisamos al usuario y le permitimos guardarlo antes de continuar. Pero primero se fija si es que hay datos
            # en pantalla.
        if Controla == True:
            self.V_C_Controla_Cambios_Guarda(Siguiente3 = False)

        # True: Cuando estamos actualizando con un excel
        if mi_vars.EXCEL == True:
            tope = len(mi_vars.Lineas)
            mi_vars.CONTADOR_ += 1
            if mi_vars.CONTADOR_ == tope:
                self.MuestraMsjOK("Se ha llegado al final de la lista (producto nro: " + str(tope) + "), se cerrará el proceso de carga.", "Fin de la lista")
                self.Deshabilita_Excel()
                self.LimpiarPantalla()
            else:
                valor = Automatico
                self.Compara_Excel_BBDD(Automatico = valor)
        
        # Operación normal
        else:

            # Avanza una posición según la ubicación del registro actual, con respecto a la base de datos
            if self.ui.line_ID.text() != "":

                Valor = int(self.ui.line_ID.text())

                if Valor < self.TOTAL:
                    self.ui.line_ID.setText(str(Valor+1))
                else:
                    # self.MuestraMsjOK("Hay " + str(self.TOTAL) + " registros. Volvemos al primero.", "Aviso")
                    self.ui.line_ID.setText('1')
            else:
                self.MuestraMsjOK("Debe haber un valor en el recuadro de ID", "Error al intentar retroceder un Registro")
                self.ui.line_ID.setFocus()

    # Permite elegir un archivo de Excel del que viene desde Essen y tiene toda la información actual para el Ciclo. El problema está que así como viene por defecto no lo 
        # puede abrir, tengo que investigar eso, porque he copiado los datos ignorando la columna A y se puede abrir el archivo. Por el contario, si copiamos la columna A
        # el archivo tampoco puede abrirse.
    def Clic_RecorreExcel(self): ###

        self.V_C_Controla_Cambios_Guarda()

        # True: Desactiva toda la actividad y coloca el programa en el estado en que estaba. False: Activa la carga de datos de Excel.
        if mi_vars.EXCEL == True:

            # Reestablecemos las variables
            self.Deshabilita_Excel()

        else:    
            # Configuramos la pantalla para el proceso de carga
            self.LimpiarPantalla()
            mi_vars.EXCEL = True
            self.ui.push_Buscar.setEnabled(False)
            self.ui.push_Limpiar.setEnabled(False)
            self.ui.push_Menu.setEnabled(False)
            icon5 = QtGui.QIcon()
            icon5.addPixmap(QtGui.QPixmap("icon/exceladvert.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            self.ui.push_Excel.setIcon(icon5)
            self.ui.push_Excel.setIconSize(QtCore.QSize(70, 70))
            
            # Abrimos la ventana para que el usuario cargue en el sistema el archivo en cuestión
            Ruta = ""
            Ruta, _ = QFileDialog.getOpenFileName(self, 'Buscar Archivo', QDir.homePath(), "All Files (*.xlsx);;All Files (*.xls);;All Files (*.ods);;All Files (*.xlt);;All Files (*)")
            
            # True: Operación normal. False: Ocurrió un error y no se ha podido encontrar la ruta
            if Ruta != "":
                
                # Le consultamos al usuario si desea que los valores se actualicen automáticamente o si quiere revisar uno por uno
                Respuesta = QMessageBox.question(self, "Actualizar los datos del Excel", "Se está por ejecutar la ACTUALIZACIÓN de la base de datos con el EXCEL.  ¿Desea que el programa actualice todo automáticamente?. \n\n Nota: Sólo se actualizarán los productos que tengan alguna diferencia y el programa se detendrá cuando encuentre un producto nuevo.", QMessageBox.Yes | QMessageBox.No)
                
                # Preparamos la información
                mi_vars.Lineas, mi_vars.Codigos, mi_vars.Descripcion, mi_vars.Pspv, mi_vars.Precio, mi_vars.Puntos, mi_vars.PuntosMG, mi_vars.Filas = exl.Dev_Listas(Ruta, "Sheet1", 'H')

                # Recorremos los códigos de la base de datos y los comparamos con los del excel y si algún producto no se encuentra en la lista
                    # de excel le cargamos su código en una lista auxiliar (LISTAAUXILIAR). Durante el bucle no podemos actualizar los valores
                    # de los productos a -> Desactivados, porque genera error de Base de datos bloqueada, ya que durante todo el bucle for la
                    # misma se encuentra abierta, por ende se hace luego.
                Tabla = mdb.Dev_Tabla(mi_vars.BaseDeDatos, 'Productos')
                LISTAAUXILIAR = []
                for reg in Tabla:
                    try:
                        print(mi_vars.Codigos.index(reg[2]))
                    except:
                        LISTAAUXILIAR.append(reg[2])
                Tabla = ""

                # Controlamos si no es que ya están desactivados
                LISTAAUXILIAR2 = []
                if len(LISTAAUXILIAR) > 0:
                    for i in LISTAAUXILIAR:
                        DatosAux = self.R_T_Retorna_Datos_De_BBDD(Codigo=i)
                        if DatosAux[1] == 1:
                            LISTAAUXILIAR2.append(DatosAux[2])
                LISTAAUXILIAR = LISTAAUXILIAR2
                # Creamos un string que va a ser el mensaje para mostrar al usuario
                Largo = len(LISTAAUXILIAR)
                if Largo > 0:
                    MensajeAmostrar = 'Se DESACTIVARÁN los siguientes productos porque no se encuentran disponibles en el ciclo vigente: \n \n'
                    for pos in LISTAAUXILIAR:
                        DatosAux = self.R_T_Retorna_Datos_De_BBDD(Codigo=pos)
                        DatosAux[1] = 0
                        self.V_T_Guarda_Actualizacion(DatosAux)
                        AuxLinea = mi_vars.LINEAORDENADA[DatosAux[3]] + " "
                        AuxTipo = mi_vars.TIPO[DatosAux[4]] + " "
                        AuxInterior = mi_vars.INTERIOR[DatosAux[5]] + " "
                        AuxRepuesto = DatosAux[6] + " "
                        AuxBazar = DatosAux[7] + " "
                        AuxAyVtas = DatosAux[8] + " "
                        AuxPedido = DatosAux[9] + " "
                        AuxOtros = DatosAux[10]
                        MensajeAmostrar = MensajeAmostrar + AuxLinea + AuxTipo + AuxInterior + AuxRepuesto + AuxBazar + AuxAyVtas + AuxPedido + AuxOtros + "\n"

                    QMessageBox.question(self, "PRODUCTOS DESACTIVADOS", MensajeAmostrar, QMessageBox.Ok)

                # True: Cuando decidió que el programa se actualice sólo. False: Se recorre producto por producto.
                if Respuesta == QMessageBox.Yes:
                    self.Compara_Excel_BBDD(Automatico=True)
                else:
                    self.Compara_Excel_BBDD()
            else:
                # Reestablecemos todo y damos aviso que no se ha podido establecer la ruta
                self.Deshabilita_Excel()
                self.MuestraMsjOK("No se ha podido cargar la RUTA del archivo especificado. Error desconocido [1556]", "Error al intentar cargar Ruta")

    # Este evento se ejecuta cada vez que se presiona una tecla ya sea tanto en la pantalla como en los line_edit especificados. La dificultad de estos casos es mostrar un 
    # número decimal correcto teniendo en cuenta qué es lo que digita el usuario, por ello capturamos lo que digita en una variable, y luego traducimos ésto al LineEdit
    # correspondientes
    def keyPressEvent(self, event): ###

        # Capturamos la tecla presionada en formato str
        Valor = event.text()

        # Le permitimos sólo valores indicados para números decimales
        Texto = fts.Devuelve_Entero_Signo(Valor)

        # Ctrl + S
        if Valor == '\x13':
            self.Clic_Siguiente()

        # LINE EDIT Precio de Costo
        elif (self.ui.line_Pcio_Costo.hasFocus()):
            # Se ejecuta cuando se apreta para borrar
            if event.key() == Qt.Key_Backspace:
                self.LINEVALOR1, AuxString = self.Ayuda_Event_Backspace(self.LINEVALOR1)
                self.ui.line_Pcio_Costo.setText(AuxString)
            elif Texto != 'F':
                self.LINEVALOR1 += Texto
                self.LINEVALOR1, AuxString = self.Ayuda_Event_Ingresan_Valores(self.LINEVALOR1)
                self.ui.line_Pcio_Costo.setText(AuxString)
                
        # LINE EDIT Costo 10
        elif (self.ui.line_Costo10.hasFocus()):
            if event.key() == Qt.Key_Backspace:
                self.LINEVALOR2, AuxString = self.Ayuda_Event_Backspace(self.LINEVALOR2)
                self.ui.line_Costo10.setText(AuxString)
            elif Texto != 'F':
                self.LINEVALOR2 += Texto
                self.LINEVALOR2, AuxString = self.Ayuda_Event_Ingresan_Valores(self.LINEVALOR2)
                self.ui.line_Costo10.setText(AuxString)

        # LINE EDIT Pspv
        elif (self.ui.line_PSPV.hasFocus()):
            if event.key() == Qt.Key_Backspace:
                self.LINEVALOR3, AuxString = self.Ayuda_Event_Backspace(self.LINEVALOR3)
                self.ui.line_PSPV.setText(AuxString)
            elif Texto != 'F':
                self.LINEVALOR3 += Texto
                self.LINEVALOR3, AuxString = self.Ayuda_Event_Ingresan_Valores(self.LINEVALOR3)
                self.ui.line_PSPV.setText(AuxString)

        # LINE EDIT Precio de Lista
        elif (self.ui.line_Pcio_Lista.hasFocus()):
            if event.key() == Qt.Key_Backspace:
                self.LINEVALOR4, AuxString = self.Ayuda_Event_Backspace(self.LINEVALOR4)
                self.ui.line_Pcio_Lista.setText(AuxString)
            elif Texto != 'F':
                self.LINEVALOR4 += Texto
                self.LINEVALOR4, AuxString = self.Ayuda_Event_Ingresan_Valores(self.LINEVALOR4)
                self.ui.line_Pcio_Lista.setText(AuxString)

    # Calcula lo que hay que hacer cuando se presiona un Backspace dentro de los lineEdit de decimales (con precios). 
        # Devuelve 2 variables, donde la primera indica el valor que debe tomar la var global y el 2do el valor en el lineEdit
    def Ayuda_Event_Backspace(self, Valor):
        largo = len(Valor)
        if largo > 1:
            if largo == 1 and Valor == '0':
                Resultado1 = ''
                Resultado2 = '0,00'
            else:
                Resultado1 = Valor[0:(largo-1)]
                Resultado2 = fts.Formato_Decimal(Resultado1,2)
        else:
            Resultado1 = ''
            Resultado2 = fts.Formato_Decimal('0',2)
        return Resultado1, Resultado2

    def Ayuda_Event_Ingresan_Valores(self, Texto):
        if Texto == '.' or Texto == ',':
            Resultado1 = '0.'
            Resultado2 = '0,00'
        elif Texto == '0':
            Resultado1 = ''
            Resultado2 = "0,00"
        else:
            Texto = fts.Ajusta_A_2_Dec(Texto)
            Resultado1 = Texto
            Resultado2 = fts.Formato_Decimal(Resultado1,2)
        return Resultado1, Resultado2

    # ======================= FUNCIONES ============================

    # Sirve sólo en modo Excel, cuando se actualiza la info, es para recorrer los códigos encontrados en el excel y ver si existen o si hay datos nuevos
        # Se maneja con el valor que tenga mi_vars.CONTADOR_, buscando coincidencia del código que figure en éste momento en la variable mi_vars.Codigos[mi_vars.CONTADOR_]
        # Si el producto no se encuentra en la base de datos, da aviso y prepara todo para realizar la creación de un nuevo registro
        # Si hay que mostar algo en pantalla se encarga de hacerlo, y sino continúa solito recorriendo los demás productos
    def Compara_Excel_BBDD(self, Automatico = False): ###
        global AUTOM_ACT
        Nuevo = False
        # La variable AUTOM_ACT contabiliza la cantidad de productos actualizados. En cada dato dispar se le suma un punto a dicha variable. Para que un mismo producto
            # que tenga varios ítems diferentes no sume varias veces el dato, usamos ésta variable local como bandera
        AvisoAutom = False
        try:
            # Sólo sirve en modo Excels
            if mi_vars.EXCEL == True:
                Diferencia = False
                CantidadProd = len(mi_vars.Lineas)
                Codigo = mi_vars.Codigos[mi_vars.CONTADOR_]

                # Buscamos su información en la bd
                # True: Cuando es un producto nuevo. False: Cuando existe ese producto
                # El producto nuevo directamente activa la variable Diferencia
                if self.R_T_Busca_ID_Cod(False, Codigo) == False:

                    # Avisa que es un producto que no existía y facilita su creación
                    self.MuestraMsjOK("El siguiente producto no existe en la base de datos. \n\n Codigo: " + Codigo + "\n Descripción: " + mi_vars.Lineas[mi_vars.CONTADOR_] + "  // " + mi_vars.Descripcion[mi_vars.CONTADOR_] + "\n\n La descripción del mismo, será cargada en la casilla de comentarios para que los utilice para controlar que se carguen bien todos sus datos.", "ATENCIÓN: NUEVO PRODUCTO")
                    Nuevo = True
                    Datos = ['0','','','','','','','','','','','','','','','','','','','','','']
                    Datos[1] = 1
                    Datos[2] = Codigo
                    Datos[3] = 0
                    Datos[4] = 0
                    Datos[5] = 0
                    Datos[6] = ''
                    Datos[7] = ''
                    Datos[8] = ''
                    Datos[9] = ''
                    Datos[10] = ''
                    Datos[11] = ''
                    Datos[12] = ''
                    Datos[13] = float(fts.Redondear(fts.Ajusta_A_2_Dec(mi_vars.Precio[mi_vars.CONTADOR_])))
                    Datos[14] = float(fts.Redondear(fts.Ajusta_A_2_Dec(mi_vars.Precio[mi_vars.CONTADOR_] * 1.1)))
                    Datos[15] = float(fts.Redondear(fts.Ajusta_A_2_Dec(mi_vars.Pspv[mi_vars.CONTADOR_])))
                    Datos[16] = float(fts.Redondear(fts.Ajusta_A_2_Dec((mi_vars.Pspv[mi_vars.CONTADOR_] * 1.1) / 12)) * 12)
                    Datos[17] = mi_vars.Puntos[mi_vars.CONTADOR_]
                    Datos[18] = mi_vars.PuntosMG[mi_vars.CONTADOR_]
                    Datos[19] = "[PRODUCTO NRO: " + str(mi_vars.CONTADOR_ + 1) + "   DE: " + str(CantidadProd) + "]  " + mi_vars.Lineas[mi_vars.CONTADOR_] + " // " + mi_vars.Descripcion[mi_vars.CONTADOR_]
                    Datos[20] = Datos[20] = "./img\\" + self.ui.line_Codigo.text() + ".png"
                    Datos[21] = self.R_T_Dev_Fecha_Act()
                    Diferencia = True
                
                else:
                    
                    # Comparamos los datos actuales con los existentes, y editamos los existentes
                    # Si hay diferencias se activa la variable Diferencia
                    
                    # Activo
                    Datos = self.R_T_Retorna_Datos_De_BBDD(Codigo=Codigo)
                    if Datos[1] == 0:
                        Diferencia = True
                        if Automatico == True:
                            AvisoAutom = True
                            AUTOM_ACT += 1
                            Datos[1] = 1
                        else:
                            Datos[1] = 1
                            self.ui.checkBox_Activo.setStyleSheet("background-color: rgb(255, 170, 127);")
                    # Precio de Costo y Costo10
                    mi_vars.Precio[mi_vars.CONTADOR_] = float(fts.Redondear(fts.Ajusta_A_2_Dec(mi_vars.Precio[mi_vars.CONTADOR_])))
                    if Datos[13] != mi_vars.Precio[mi_vars.CONTADOR_]:
                        Diferencia = True
                        if Automatico == True:
                            Datos[13] = mi_vars.Precio[mi_vars.CONTADOR_]
                            Datos[14] = float(fts.Redondear(fts.Ajusta_A_2_Dec(mi_vars.Precio[mi_vars.CONTADOR_]*1.1)))
                            if AvisoAutom == False:
                                AvisoAutom = True
                                AUTOM_ACT += 1
                        else:
                            Datos[13] = mi_vars.Precio[mi_vars.CONTADOR_]
                            Datos[14] = float(fts.Redondear(fts.Ajusta_A_2_Dec(mi_vars.Precio[mi_vars.CONTADOR_]*1.1)))
                            self.ui.line_Pcio_Costo.setStyleSheet("background-color: rgb(255, 170, 127);")
                            self.ui.line_Costo10.setStyleSheet("background-color: rgb(255, 170, 127);")
                    # PSPV y Pcio Lista
                    if Datos[15] != mi_vars.Pspv[mi_vars.CONTADOR_]:
                        Diferencia = True
                        if Automatico == True:
                            Datos[15] = float(fts.Redondear(fts.Ajusta_A_2_Dec(mi_vars.Pspv[mi_vars.CONTADOR_])))
                            Datos[16] = float((fts.Redondear((Datos[15] * 1.1) / 12)) * 12)
                            if AvisoAutom == False:
                                AvisoAutom = True
                                AUTOM_ACT += 1
                        else:
                            Datos[15] = float(fts.Redondear(fts.Ajusta_A_2_Dec(mi_vars.Pspv[mi_vars.CONTADOR_])))
                            Datos[16] = float((fts.Redondear((Datos[15] * 1.1) / 12)) * 12)
                            self.ui.line_PSPV.setStyleSheet("background-color: rgb(255, 170, 127);")
                            self.ui.line_Pcio_Lista.setStyleSheet("background-color: rgb(255, 170, 127);")
                    # Puntos
                    if Datos[17] != mi_vars.Puntos[mi_vars.CONTADOR_]:
                        Diferencia = True
                        if Automatico == True:
                            Datos[17] = mi_vars.Puntos[mi_vars.CONTADOR_]
                            if AvisoAutom == False:
                                AvisoAutom = True
                                AUTOM_ACT += 1
                        else:
                            Datos[17] = mi_vars.Puntos[mi_vars.CONTADOR_]
                            self.ui.line_Puntos.setStyleSheet("background-color: rgb(255, 170, 127);")
                    # Puntos MG
                    if Datos[18] != mi_vars.PuntosMG[mi_vars.CONTADOR_]:
                        Diferencia = True
                        if Automatico == True:
                            Datos[18] = mi_vars.PuntosMG[mi_vars.CONTADOR_]
                            if AvisoAutom == False:
                                AvisoAutom = True
                                AUTOM_ACT += 1
                        else:
                            Datos[18] = mi_vars.PuntosMG[mi_vars.CONTADOR_]
                            self.ui.line_Puntos_MG.setStyleSheet("background-color: rgb(255, 170, 127);")
                    if Diferencia == True:
                        Datos[19] = "[PRODUCTO NRO: " + str(mi_vars.CONTADOR_ + 1) + "   DE: " + str(CantidadProd) + "]"
                
                if Automatico == True:
                    if Diferencia == True:
                        # Si Nuevo = True: Se muestran los datos. Si Nuevo = False, se guardan cambios y se continúa.
                        if Nuevo == True:
                            self.V_T_Cargar_Datos(Datos, Nuevo=True)
                        else:
                            self.V_T_Guarda_Actualizacion(Datos)
                            self.Clic_Siguiente(Automatico = True)
                    else:
                        self.Clic_Siguiente(Automatico = True)
                else:
                    # Si la variable Diferencia está en True, es porque hay un producto nuevo o hay diferencias entre los datos del excel y los de la bd, en ambos casos
                        # tenemos que mostrar en pantallas los valores. Y sino, se pasa al siguiente producto
                    if Diferencia == True:
                        if Nuevo == True:
                            self.V_T_Cargar_Datos(Datos, Nuevo = True)
                        else:
                            self.V_T_Cargar_Datos(Datos)
                    else:
                        self.Clic_Siguiente(Automatico = False)
        except:
            self.MuestraMsjOK("Se ha producido un error innesperado al intentar comparar la base de datos con los datos del archivo de Excel. Error [34555]", "Error")

    # Se cargan los datos de la BBDD y de la ventana en diferentes listas y luego se las compara
    def R_T_Compara_Ventana_BBDD(self, Id_): ###

        # Cargamos los datos de la BBDD en la lista Datos1
        Datos1 = self.R_T_Retorna_Datos_De_BBDD(ID = Id_)
        # Cargamos los datos de la ventana en la lista Datos2
        Datos2 = self.R_T_Convierte_Datos_Para_BD(self.R_T_Retorna_Datos_De_Ventana())

        # Por defecto cuando miramos el excel se modifica el comentario, por ende siempre será distinto
        if mi_vars.EXCEL == True:
            Datos1[19] = ''
            Datos2[19] = ''
        # No se comparan las imagenes porque en sí es un dato que se crea con código, no es un dato que se esté utilizando por el momento.
        Datos1[20] = Datos2[20]
        # No se comparan las fechas, porque no son datos que el usuario modifica, por ende no se puede interpretar como un cambio sin guardar.
        # Además, sucede que la comparación de fechas siempre da distinto cuando el útlimo guardado pertenece a otro día del actual.
        Datos1[21] = ''
        Datos2[21] = ''
        
        if self.R_T_Compara_Listas(Datos1, Datos2) == 3:
            return True
        else:
            return False

    def Deshabilita_Excel(self): ###

        mi_vars.EXCEL = False
        mi_vars.CONTADOR_ = 0
        mi_vars.Lineas = []
        mi_vars.Codigos = []
        mi_vars.Descripcion = []
        mi_vars.Pspv = []
        mi_vars.Precio = []
        mi_vars.Puntos = []
        mi_vars.PuntosMG = []
        mi_vars.Filas = []

        # Reestablecemos la pantalla
        self.Devuelve_Fondos()
        self.ui.push_Buscar.setEnabled(True)
        self.ui.push_Limpiar.setEnabled(True)
        self.ui.push_Menu.setEnabled(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ui.push_Excel.setIcon(icon5)
        self.ui.push_Excel.setIconSize(QtCore.QSize(70, 70))

    # Cuando se trabaja con el Excel, se pintan los fondos de los line_edit donde hubieron modificaciones, es decir, que si un producto que está cargado en la base de datos
        # viene con precios nuevos pero es lo único que cambió, entonces los fondos de los line_edit se pintan de otro color y por ejemplo los de los puntos se mantienen igual.
        # Lo que hace ésta función es devolverles el color normal luego de ser tratados con ese cambio antes explicado.
    def Devuelve_Fondos(self): ###
        self.ui.line_Tamanio.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.line_Litros.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.line_Pcio_Costo.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.ui.line_Costo10.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.ui.line_PSPV.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.ui.line_Pcio_Lista.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.ui.line_Puntos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.line_Puntos_MG.setStyleSheet("background-color: rgb(255, 255, 255);")


    '''########################################################################################################################################
    ###########################################################################################################################################
                                                        FUNCIONES GENERALES                                                             
        Son funciones que ayudan a todas en general a trabajar
        '''
    # Compara 2 listas, y devuelve:
        # 0: Si hubo algún error
        # 1: Si las listas no tienen el mismo tamaño
        # 2: Si no hubo diferencias
        # 3: Si encontró diferencias
    def R_T_Compara_Listas(self, Lista1,Lista2): ###
        # Si ocurre algún error, salta al except que retorna 0
        try:

            # Controlamos que tengan ambas el mismo largo, retornamos 1
            Largo1 = len(Lista1)
            Largo2 = len(Lista2)
            if Largo1 != Largo2:
                return 1
            
            # Controlamos la información que contiene, si hay diferencias retornamos 3
            Bucle = 0
            while Bucle < Largo1:
                if Lista1[Bucle] != Lista2[Bucle]:
                    return 3
                Bucle += 1
            
            # Si llegamos acá, es porque estuvo todo correcto y no hay diferencias, retornamos 2
            return 2

        except:
            return 0

    # Convierte la fecha actual al mes corriente, para ser guardado en la base de datos
    def R_T_Dev_Fecha_Act(self):
        dt = datetime.now()
        Resultado = str(dt.year) + '/' + str(dt.month) + '/' + str(dt.day)
        return Resultado





    '''########################################################################################################################################
    ###########################################################################################################################################
                                                    FUNCIONES PARA MANIPULACIÓN DE DATOS                                                    

    Los datos a manipular son aquellos que contiene cada producto. Se pueden tomar datos desde la ventana (que su tipo de dato es string) o desde la base de datos (que 
    son de todo tipo de datos según sea su importancia), los mismos tienen diferentes formatos así que necesitamos funciones para obtener los datos, comparar los datos
    y guardar los datos. Además si vamos a compararlos para buscar diferencias entre sus valores, se van a realizar en el formato de BD y no de string como ventana.

    REALACIÓN DE DATOS
        Datos[0]    ID
        Datos[1]    Activo
        Datos[2]    Codigo
        Datos[3]    Linea
        Datos[4]    Tipo
        Datos[5]    Interior
        Datos[6]    Repuestos
        Datos[7]    Concepto de Bazar
        Datos[8]    Concepto de Ayuda ventas
        Datos[9]    Pedidos especiales
        Datos[10]    Otros
        Datos[11]    Tamanio
        Datos[12]    Litros
        Datos[13]   Precio de Costo
        Datos[14]   Precio de Costo mas el 10%
        Datos[15]   PSPV
        Datos[16]   Precio de Lista
        Datos[17]   Puntos
        Datos[18]   Puntos MG
        Datos[19]   Comentarios
        Datos[20]   Path de Imagen
        Datos[21]   Fecha actualización
    '''

    # Se encarga de crear una lista con todos los datos que tenemos en la ventana.
    def R_T_Retorna_Datos_De_Ventana(self):
        Datos = ['0','','','','','','','','','','','','','','','','','','','','','']
        Datos[0] = self.ui.line_ID.text()
        Datos[1] = self.ui.checkBox_Activo.isChecked()
        Datos[2] = self.ui.line_Codigo.text()
        Datos[3] = self.ui.comboBox_Linea.currentIndex()
        Datos[3] = mi_vars.LINEANUM[Datos[3]]
        Datos[4] = self.ui.comboBox_Tipo.currentIndex()
        Datos[5] = self.ui.comboBox_Interior.currentIndex()
        Datos[6] = self.ui.line_Repuesto.text()
        Datos[7] = self.ui.line_Bazar.text()
        Datos[8] = self.ui.line_Ayudavta.text()
        Datos[9] = self.ui.line_Pedido.text()
        Datos[10] = self.ui.line_Otros.text()
        Datos[11] = self.ui.line_Tamanio.text()
        Datos[12] = self.ui.line_Litros.text()
        Datos[13] = self.ui.line_Pcio_Costo.text()
        Datos[14] = self.ui.line_Costo10.text()
        Datos[15] = self.ui.line_PSPV.text()
        Datos[16] = self.ui.line_Pcio_Lista.text()
        Datos[17] = self.ui.line_Puntos.text()
        Datos[18] = self.ui.line_Puntos_MG.text()
        Datos[19] = self.ui.textEdit_Comentarios.toPlainText()
        Datos[20] = "./img\\" + self.ui.line_Codigo.text() + ".png"
        Datos[21] = self.R_T_Dev_Fecha_Act()
        return Datos

    # Convierte los datos de una lista que viene de datos de la ventana al formato que utiliza la base de datos, como muchos datos se mantienen no se tocan
    def R_T_Convierte_Datos_Para_BD(self, Datos):
        if Datos[0] != '':
            Datos[0] = int(Datos[0])
        Datos[1] = int(Datos[1])
        Datos[13] = fts.Str_Float(Datos[13])
        Datos[14] = fts.Str_Float(Datos[14])
        Datos[15] = fts.Str_Float(Datos[15])
        Datos[16] = fts.Str_Float(Datos[16])
        if Datos[17] != "":
            Datos[17] = int(Datos[17])
        else:
            Datos[17] = 0
        if Datos[18] != "":
            Datos[18] = int(Datos[18])
        else:
            Datos[18] = 0
        return Datos

    # Cuando se necesitan los datos de la BBDD aquí los obtenemos ya sea según su ID o código y los retorna.
    # Si hubo error en los datos que llegaron como parámetro la posición cero tendrá un cero en formato string. Y tendrá un '1' (string) si no pudo encontrar los datos.
    def R_T_Retorna_Datos_De_BBDD(self, ID = 0, Codigo = 0):
        Datos = ['0','','','','','','','','','','','','','','','','','','','','','']
        if (ID != 0 and Codigo != 0) or (ID == 0 and Codigo == 0):
            print("[ERROR INTERNO 887]")
        else:
            if ID != 0:
                fila = mdb.Reg_Un_param(mi_vars.BaseDeDatos,'Productos', "ID", ID)
            else:
                fila = mdb.Reg_Un_param(mi_vars.BaseDeDatos,'Productos', "Codigo", Codigo)
                
            for pos in fila:
                Datos = [pos[0],pos[1],pos[2],pos[3],pos[4],pos[5],pos[6],pos[7],pos[8],pos[9],pos[10],pos[11],pos[12],pos[13],pos[14],pos[15],pos[16],pos[17],pos[18],pos[19],pos[20],pos[21]]
            if Datos[0] == '0':
                Datos[0] = '1'
            else:
                # A imagenes les colocamos sólo el nombre de código
                Datos[20] = str(Datos[2])
        return Datos

    # Convierte los datos de una lista que viene de la bd al formato que utiliza la ventana. Como muchos formatos se mantienen no se tocan
    def R_T_Convierte_Datos_Para_Ventana(self, Datos):
        Datos[0] = str(Datos[0])
        if Datos[1] == 0:
            Datos[1] = False
        else:
            Datos[1] = True
        Datos[13] = fts.Formato_Decimal(Datos[13],2)
        Datos[14] = fts.Formato_Decimal(Datos[14],2)
        Datos[15] = fts.Formato_Decimal(Datos[15],2)
        Datos[16] = fts.Formato_Decimal(Datos[16],2)
        Datos[17] = str(Datos[17])
        Datos[18] = str(Datos[18])
        Datos[21] = fts.Devuelve_Mes_Texto(fts.Devuelve_Valor_Mes(Datos[21]))
        return Datos

    # Controla los Datos para saber si el usuario quiere guardar o crear un producto.
        # 0: Error o no se quiere guardar nada
        # 1: Se quiere GUARDAR
        # 2: Se quiere CREAR
    def R_T_Verifica_Datos_Guardar_Crear(self, Id_, Codigo_):
        # Convertimos ID por las dudas venga en formato string. Con código no nos preocupamos porque en todo momento se trabaja en formato string.
        if Id_ == '' or Id_ == '0':
            Id_ = ''
        else:
            Id_ = int(Id_)
        # Si tiene un valor ID, sólo se pueden guardar cambios, sino, entonces es un producto nuevo
        if Id_ != "":
            # Hay un valor ingresado, ahora vamos a corroborar que exista, sino, el usuario puede estar queriendo crear un archivo nuevo
            if self.R_T_Busca_ID_Cod(True, Id_) == True:
                # Debido a que el código de un producto es importante, vamos a corroborar que el ID coincida con el CODIGO. En caso de no coincidir damos aviso de que
                    # dicho dato será modificado.
                if self.R_T_Controla_ID_Cod(Id_, Codigo_) != 3:
                    self.MuestraMsjOK('','',9)
                return 1
            else:
                self.MuestraMsjOK('','',1)
                return 0
        else:
            # Si tiene un valor Codigo, se puede crear, pero si quiere guardar debería tener el ID correctamente, y si llega a ésta instancia es porque el ID está vacío
            if Codigo_ != "":
                # Hay un valor ingresado, ahora vamos a corroborar que exista, sino, el usuario puede estar queriendo crear un archivo nuevo
                if self.R_T_Busca_ID_Cod(False, Codigo_) == True:
                    self.MuestraMsjOK('', '', 1)
                    return 0
                else:
                    return 2
            else:
                self.MuestraMsjOK('','',10)
                return 0

    # Controla los Datos para saber si se puede guardar los cambios del producto que se observa. Se supone que a ésta función se la llama con un ID y un valor de Codigo.
        # VALORES DE RETORNO:
        # 0: Error al intentar hacer la operación
        # 1: Error donde los datos cargados son insuficientes o erróneos. De igual modo ésta función se encarga de dar aviso al usuario.
        # 2: No hay diferencias con la base de datos, innecesario guardar
        # 3: Hay diferencias y se quieren guardar
        # 4: Hay diferencias pero no se van a guardar

        # Nota: Hay valores tanto como los puntos como los detalles que no siempre están disponibles ni serían obligación, pero como en algunos productos están y cuando
            # están son muy importantes, lo que hacemos es obligar al usuario que pase por el valor y lo controle y cargue aunque sea un valor nulo para que preste 
            # atención al mismo.
    def R_T_Control_Datos_Guardar(self, ListaDatos, Mensaje = True):
        # Parte0
        try:
            # Parte1
            # Vamos a corroboarar que haya ID y Codigo
            if ListaDatos[0] == '' or ListaDatos[2] == '':
                self.MuestraMsjOK('','',1)
            
            Parte1 = 0
            # Controlamos los datos del recuadro de Concepto/Tipo
            if ListaDatos[3] > 0:
                Parte1 += 1
            if ListaDatos[4] > 0:
                Parte1 += 1
            if ListaDatos[5] > 0:
                Parte1 += 1
            if Parte1 == 0:
                if ListaDatos[6] != '':
                    Parte1 += 1
                if ListaDatos[7] != '':
                    Parte1 += 1
                if ListaDatos[8] != '':
                    Parte1 += 1
                if ListaDatos[9] != '':
                    Parte1 += 1
                if ListaDatos[10] != '':
                    Parte1 += 1
                if Parte1 != 1:
                    self.MuestraMsjOK('','',2)
                    return 1
            elif Parte1 == 3:
                if ListaDatos[6] != '' or ListaDatos[7] != '' or ListaDatos[8] != '' or ListaDatos[9] != '' or ListaDatos[10] != '':
                    self.MuestraMsjOK('','',2)
                    return 1
            else:
                self.MuestraMsjOK('','',3)
                return 1

            # Si hay una pieza seleccionada controlamos que coloquen los DETALLES
            if ListaDatos[3] > 1:
                if ListaDatos[11] == '' or ListaDatos[12] == '':
                    self.MuestraMsjOK('','',4)
                    return 1
            
            # Controlamos los Costos
            if ListaDatos[13] == '':
                self.MuestraMsjOK('','',5)
                return 1
            if ListaDatos[14] == '':
                self.MuestraMsjOK('','',5)
                return 1
            if ListaDatos[15] == '':
                self.MuestraMsjOK('','',5)
                return 1
            if ListaDatos[16] == '':
                self.MuestraMsjOK('','',5)
                return 1
            
            # Controlamos los puntos
            if ListaDatos[17] == '':
                self.MuestraMsjOK('','',6)
                return 1
            if ListaDatos[18] == '':
                self.MuestraMsjOK('','',6)
                return 1
            
            # Parte2
            # Comparamos los datos tanto en pantalla con la bd para saber si hubieron cambios
            ListaAux1 = self.R_T_Retorna_Datos_De_BBDD(ID=ListaDatos[0])
            # Estos datos no importan si difieren. Por ej el 19 (comentarios) siempre difieren cuando se carga un EXCEL y 21 (fecha Act) por otro lado también difiere.
            if mi_vars.EXCEL == True:
                ListaDatos[19] == ListaAux1[19]
            ListaAux1[20] == ListaDatos[20]
            ListaAux1[21] == ListaDatos[21]
            Retorno = self.R_T_Compara_Listas(ListaAux1, ListaDatos)
            if Retorno == 2:
                self.MuestraMsjOK('','',7)
            
            # Parte3
            # La variable Mensaje viene arrastrada de 2 funciones atrás, donde se le ha preguntado al usuario si quiere guardar los cambios. Como ya se le preguntó y dijo
                # que sí, acá no volvemos a hacerlo. En todos los demás casos sí se consulta al usuario si quiere guardar los cambios.
            if Mensaje == True:
                # Si pasó por todos los controles, podemos consultar si va a cargar los datos
                Texto = "Está por guardar los cambios, ¿está seguro/a que desea sobreescribir los datos del producto?"
                Respuesta = QMessageBox.question(self, "Confirmar", Texto, QMessageBox.Yes | QMessageBox.No)
                if Respuesta == QMessageBox.Yes:
                    return 3
                else:
                    return 4
            else:
                return 3
        except:
            # Parte0
            return 0

    # Controla los Datos para saber si se puede guardar los cambios del producto que se observa. Se supone que a ésta función se la llama sin ID y con un valor de Codigo.
        # VALORES DE RETORNO:
        # 0: Error al intentar hacer la operación
        # 1: Error el código ya existe
        # 2: Error donde los datos cargados son insuficientes o erróneos. De igual modo ésta función se encarga de dar aviso al usuario.
        # 3: Se van a guardar los cambios
        # 4: No se van a guardar

        # Nota: Hay valores tanto como los puntos como los detalles que no siempre están disponibles ni serían obligación, pero como en algunos productos están y cuando
            # están son muy importantes, lo que hacemos es obligar al usuario que pase por el valor y lo controle y cargue aunque sea un valor nulo para que preste 
            # atención al mismo.
    def R_T_Control_Datos_Crear(self, ListaDatos, Mensaje = True):
        # Parte0
        try:
            # Parte1
            # Vamos a corroborar que el Codigo no exista
            if self.R_T_Busca_ID_Cod(False, ListaDatos[2]) == True:
                self.MuestraMsjOK('','',8)
                return 1
            
            # Parte2
            Parte2 = 0
            # Controlamos los datos del recuadro de Concepto/Tipo
            if ListaDatos[3] > 0:
                Parte2 += 1
            if ListaDatos[4] > 0:
                Parte2 += 1
            if ListaDatos[5] > 0:
                Parte2 += 1
            if Parte2 == 0:
                if ListaDatos[6] != '':
                    Parte2 += 1
                if ListaDatos[7] != '':
                    Parte2 += 1
                if ListaDatos[8] != '':
                    Parte2 += 1
                if ListaDatos[9] != '':
                    Parte2 += 1
                if ListaDatos[10] != '':
                    Parte2 += 1
                if Parte2 != 1:
                    self.MuestraMsjOK('','',2)
                    return 1
            elif Parte2 == 3:
                if ListaDatos[6] != '' or ListaDatos[7] != '' or ListaDatos[8] != '' or ListaDatos[9] != '' or ListaDatos[10] != '':
                    self.MuestraMsjOK('','',2)
                    return 1
            else:
                self.MuestraMsjOK('','',3)
                return 1

            # Si hay una pieza seleccionada entonces obligamos a que coloquen DETALLES
            if ListaDatos[3] > 1:
                if ListaDatos[11] == '' or ListaDatos[12] == '':
                    self.MuestraMsjOK('','',4)
                    return 1
            
            # Controlamos los Costos
            if ListaDatos[13] == '':
                self.MuestraMsjOK('','',5)
                return 1
            if ListaDatos[14] == '':
                self.MuestraMsjOK('','',5)
                return 1
            if ListaDatos[15] == '':
                self.MuestraMsjOK('','',5)
                return 1
            if ListaDatos[16] == '':
                self.MuestraMsjOK('','',5)
                return 1
            
            # Controlamos los puntos
            if ListaDatos[17] == '':
                self.MuestraMsjOK('','',6)
                return 1
            if ListaDatos[18] == '':
                self.MuestraMsjOK('','',6)
                return 1

            if Mensaje == True:
                # Parte 3 y 4
                # Si pasó por todos los controles, podemos consultar si va a cargar los datos
                Texto = "Está por crear un nuevo producto, ¿está seguro/a que desea guardar los datos?"
                Respuesta = QMessageBox.question(self, "Confirmar", Texto, QMessageBox.Yes | QMessageBox.No)
                if Respuesta == QMessageBox.Yes:
                    return 3
                else:
                    return 4
            else:
                return 3
        except:
            # Parte0
            return 0

    #Controla si el ID y el Codigo pertenecen al mismo producto.
        # RESULTADOS:
        # 0: Hubo algún error
        # 1: No existe el producto porque no existe el ID y el Código
        # 2: No coinciden ID y Código
        # 3: Coincidencia correcta
    def R_T_Controla_ID_Cod(self, Id_, Cod_):
        try:
            # Capturamos los datos según ID
            Id_ = int(Id_)
            Datos1 = ['0','0']
            fila1 = mdb.Reg_Un_param(mi_vars.BaseDeDatos,'Productos', "ID", Id_)
            for pos in fila1:
                Datos1 = [pos[0], pos[2]]
            # Capturamos los datos según Codigo
            Cod_ = str(Cod_)
            Datos2 = ['0','0']
            fila2 = mdb.Reg_Un_param(mi_vars.BaseDeDatos,'Productos', "Codigo", Cod_)
            for pos in fila2:
                Datos2 = [pos[0], pos[2]]

            # Analizamos y retornamos valores
            # Si no existe el producto
            if Datos1[0] == '0' and Datos2[0] == '0':
                return 1
            # No coinciden los datos de ambos valores
            if Datos1[0] != Datos2[0] or Datos1[1] != Datos2[1]:
                return 2
            # Uno de ambos valores no retornó un producto
            if Datos1[0] == '0' or Datos2[0] == '0':
                return 2
            # Todo Correcto!
            if Datos1[0] == Datos2[0] and Datos1[1] == Datos2[1]:
                return 3
        except:
            return 0

    # Devuelve True o False si es que se pudo encontrar el registro buscado, en función al ID o al Código. Es para saber si tal producto existe o no.
    def R_T_Busca_ID_Cod(self, Id_Cod_V_F, Valor):
        Datos = ['0']
        if Id_Cod_V_F == True:
            fila = mdb.Reg_Un_param(mi_vars.BaseDeDatos,'Productos', "ID", Valor)
        else:
            fila = mdb.Reg_Un_param(mi_vars.BaseDeDatos,'Productos', "Codigo", Valor)
        
        for pos in fila:
            Datos = [pos[0]]
        if Datos[0] == '0':
            return False
        else:
            return True

    # Se encarga de mostrar mensajes. Los que están ennumerados están preparados para mostrar mensajes para el control de datos
    def MuestraMsjOK(self, Mensaje, Titulo, ValorMsj = 0):
        if ValorMsj > 0:
            Titulo2 = "Error al intentar Guardar"
            if ValorMsj == 1:
                Mensaje2 = "Si desea guardar un cambio, debe cargar un ID y un CÓDIGO.\n Si desea crear un Registro nuevo, no debe cargar el valor del ID, porque se crea de manera automática. \n Para reiniciar los datos limpie la pantalla y vuelva a buscar el producto."
            elif ValorMsj == 2:
                Mensaje2 = "LÍNEA, TIPO e INTERIOR corresponde a una única clasificación, y luego están REPUESTO, BAZAR, AYUDAVENTAS, PEDIDOS ESPECIALES y OTROS. Son 6 clasificaciones en total y un producto debe tener únicamente una de ellas."
            elif ValorMsj == 3:
                Mensaje2 = "Si desea Guardar o Crear un producto, debe establecer su CONCEPTO/TIPO. Si es una PIEZA, debe contener los 3 tipos, LÍNEA, TIPO e INTERIOR. De lo contrario, debe tener una única descripción en sólo una de las 5 clasificaciones que le siguen (REPUESTO, BAZAR, AYUDAVENTAS, PEDIDOS ESP. u OTROS)."
            elif ValorMsj == 4:
                Mensaje2 = "Si se desea Crear o Guardar un producto que corresponde a los tipos de Cacerolas, Sartenes o Biferas (Piezas), es necesario cargar su Tamaño en Cm y los litros. Si dicho dato no existe, se puede cargar un valor nulo como un guión (-) o un cero (0)."
            elif ValorMsj == 5:
                Mensaje2 = "El recuadro de COSTOS debe tener todos los valores cargados."
            elif ValorMsj == 6:
                Mensaje2 = "El recuadro de PUNTOS debe tener todos los valores cargados. En caso de que el producto no tenga puntos, se puede colocar cero (0)."
            elif ValorMsj == 7:
                Mensaje2 = "No hay cambios para guardar."
            elif ValorMsj == 8:
                Mensaje2 = "El código ya pertenece a un producto, si desea editarlo debe limpiar la pantalla y volver a buscarlo, ya que si desea guardar los cambios su ID y su CÓDIGO deben coincidir."
            elif ValorMsj == 9:
                Mensaje2 = "El cambio que está por guardar modifica el CÓDIGO del producto. Éste dato es muy importante, por ello es que damos aviso para que lo controle y lo guarde correctamente. \n Si está intentando CREAR un producto nuevo, deje vacío el casillero de ID."
            elif ValorMsj == 10:
                Mensaje2 = "Para poder GUARDAR un cambio o CREAR un producto nuevo, debe al menos colocar su CÓDIGO."
        else:
            Titulo2 = Titulo
            Mensaje2 = Mensaje
        
        QMessageBox.question(self, Titulo2, Mensaje2, QMessageBox.Ok)

    # Busca un producto según ID o CODIGO, según se indique por parámetro, y luego se carga en pantalla.
        # Si bien no hay código relacionado con su "return", de todas formas devuelve 0 en caso de haber algún error
    def V_C_Muestra_Producto_Ventana(self, ValorID = '0', ValorCod = '0'):
        try:
            # Búsqueda por ID
            if ValorID != '0':
                Lista = R_T_Retorna_Datos_De_BBDD(ID=ValorID)

            # Búsqueda por Codigo
            elif ValorCod != '0':
                Lista = R_T_Retorna_Datos_De_BBDD(Codigo=ValorCod)
        
            # Si no hubo registro, entonces limpiamos la pantalla dejando el código o el id que se haya ingresado para intentar buscar. Sino cargamos todo
            if Lista[0] == '0':
                if ValorID > 0:
                    self.LimpiarPantalla(1)
                else:
                    self.LimpiarPantalla(2)
            else:
                self.V_T_Cargar_Datos(Datos)
        # Error
        except:
            return 0

    # Toma una lista y la convierte en un registro nuevo de la bd
    def V_T_Guarda_Producto_Nuevo(self, Datos):
        Activo = Datos[1]
        Codigo = Datos[2]
        Linea = Datos[3]
        Tipo = Datos[4]
        Interior = Datos[5]
        Repuesto = Datos[6]
        ConceptoBazar = Datos[7]
        ConceptoAyVta = Datos[8]
        PedidoEsp = Datos[9]
        Otros = Datos[10]
        Tamanio = Datos[11]
        Litros = Datos[12]
        PcioCosto = Datos[13]
        Costo10 = Datos[14]
        PSPV = Datos[15]
        PcioLista = Datos[16]
        Puntos = Datos[17]
        PuntosMG = Datos[18]
        # Ajustes que se hacen si se están tratando archivos de Excel
        if mi_vars.EXCEL == True:
            Comentarios = ''
            self.Devuelve_Fondos()
        else:
            Comentarios = Datos[19]
        Imagen = Datos[20]
        Actualizado = Datos[21]
        self.TOTAL += 1
        mdb.Reg_Add(mi_vars.BaseDeDatos, Activo, Codigo, Linea, Tipo, Interior, Repuesto, ConceptoBazar, ConceptoAyVta, PedidoEsp, Otros,Tamanio, Litros, PcioCosto, Costo10, PSPV, PcioLista, Puntos, PuntosMG, Comentarios, Imagen, Actualizado)
        mdb.Act_Reg_Cant(mi_vars.BaseDeDatos, self.TOTAL, 'Productos')

    # Toma una lista y la utiliza para actualizar un registro en función a su ID
    # Nota: Los datos tienen que venir listos para guardar en Base de datos
    def V_T_Guarda_Actualizacion(self, Datos):
        ID = Datos[0]
        Activo = Datos[1]
        Codigo = Datos[2]
        Linea = Datos[3]
        Tipo = Datos[4]
        Interior = Datos[5]
        Repuesto = Datos[6]
        ConceptoBazar = Datos[7]
        ConceptoAyVta = Datos[8]
        PedidoEsp = Datos[9]
        Otros = Datos[10]
        Tamanio = Datos[11]
        Litros = Datos[12]
        PcioCosto = Datos[13]
        Costo10 = Datos[14]
        PSPV = Datos[15]
        PcioLista = Datos[16]
        Puntos = Datos[17]
        PuntosMG = Datos[18]
        # Ajustes que se hacen si se están tratando archivos de Excel
        if mi_vars.EXCEL == True:
            Comentarios = ''
            self.Devuelve_Fondos()
        else:
            Comentarios = Datos[19]
        Imagen = Datos[20]
        Actualizado = Datos[21]

        mdb.Act_Reg_Prod(mi_vars.BaseDeDatos, ID, Activo, Codigo, Linea, Tipo, Interior, Repuesto, ConceptoBazar, ConceptoAyVta, PedidoEsp, Otros, Tamanio, Litros, PcioCosto, Costo10, PSPV, PcioLista, Puntos, PuntosMG, Comentarios, Imagen, Actualizado)


    '''########################################################################################################################################
    ###########################################################################################################################################
                                                    FUNCIONES RELATIVAS A LA PANTALLA                                                       '''

    # Cuando se está trabajando en la ventana de PRODUCTOS y el usuario realizó cambios y no los guardó, puede ejecutar todo tipo de acciones que hagan perder esos cambios. 
        # Por eso en ésta función se encarga de controlarlo y si hay cambios que guardar le consulta al usuario si los quiere guardar. De ser así se guardan los cambios y 
        # se vuelve a la actividad que se estaba ejecutando. Basandose en el ID y el CODIGO, si no hay datos en esas casillas ignora la acción.
        # Hay una función que hace algo parecido (self.V_C_Verifica...), pero tiene muchos mensajes de alerta que no corresponden con ésta actividad.
    def V_C_Controla_Cambios_Guarda(self, Siguiente2 = False, Siguiente3 = True):
        # Si no hay ID ni Codigo, no se hace nada. Tener en cuenta que si hay ID pero código no, tampoco se contempla
        if self.ui.line_ID.text() != '' or self.ui.line_Codigo.text() != '':
        
            # Si no hay un ID pero hay codigo, tiene que ser un producto nuevo, de ser así directamente se avisa eso.
            if self.ui.line_ID.text() == '' and self.ui.line_Codigo.text() != '':
                Datos = ['0']
                fila = mdb.Reg_Un_param(mi_vars.BaseDeDatos,'Productos', 'Codigo', self.ui.line_Codigo.text())
                # En caso de existir el producto en la base de datos (cosa que no debería suceder porque tendría que haber un ID), lo que vamos a hacer al consultarla si existe
                    # dicho código en la bd, es almacenar su ID, entonces, en caso de existir dicho producto le rellenamos el ID que le corresponde
                for pos in fila:
                    Datos = [pos[0]]
                
                # True: Cuando no existe el código. False: Existe el código en la base de datos
                if Datos[0] == '0':
                    Respuesta = QMessageBox.question(self, "Guardar Cambios", "Se encontró cargado un CÓDIGO que no existe en la base de datos, si está cargando un producto nuevo, ¿desea guardar los cambios?", QMessageBox.Yes | QMessageBox.No)
                    if Respuesta == QMessageBox.Yes:
                        self.Clic_Guardar(Siguiente2, Mensaje = False, Siguiente3=Siguiente3)
                    else:
                        self.LimpiarPantalla()
                else:
                    self.LINE_ID_ACTIVO = False
                    self.ui.line_ID.setText(str(Datos[0]))
                    self.LINE_ID_ACTIVO = True
                    # La función devuelve True si los datos en pantalla difieren de la bd
                    if self.R_T_Compara_Ventana_BBDD(Datos[0]) == True:
                        Respuesta = QMessageBox.question(self, "Guardar Cambios", "Se registraron cambios en los datos de éste producto, ¿Desea guardarlos antes de continuar?", QMessageBox.Yes | QMessageBox.No)
                        if Respuesta == QMessageBox.Yes:
                            self.Clic_Guardar(Siguiente2, Mensaje = False, Siguiente3=Siguiente3)
                        else:
                            self.LimpiarPantalla()
            
            # Si hay un ID y un CÓDIGO, es porque es un producto en existencia
            elif self.ui.line_ID.text() != '' and self.ui.line_Codigo.text() != '':
            
                # La función devuelve True si los datos en pantalla difieren de la bd
                if self.R_T_Compara_Ventana_BBDD(int(self.ui.line_ID.text())) == True:
                    Respuesta = QMessageBox.question(self, "Guardar Cambios", "Se registraron cambios en los datos de éste producto, ¿Desea guardarlos antes de continuar?", QMessageBox.Yes | QMessageBox.No)
                    if Respuesta == QMessageBox.Yes:
                        self.Clic_Guardar(Siguiente2 = Siguiente2, Mensaje = False, Siguiente3=Siguiente3)
                    else:
                        self.LimpiarPantalla()

    def LimpiarPantalla(self, LineLibre = 0):
        self.LINE_ID_ACTIVO = False
        self.LINE_COD_ACTIVO  = False
        if LineLibre != 1:
            self.ui.line_ID.clear()
        if LineLibre != 2:
            self.ui.line_Codigo.clear()
        self.ui.checkBox_Activo.setChecked(False)
        self.ui.comboBox_Linea.setCurrentIndex(0)
        self.ui.comboBox_Tipo.setCurrentIndex(0)
        self.ui.comboBox_Interior.setCurrentIndex(0)
        self.ui.line_Repuesto.clear()
        self.ui.line_Bazar.clear()
        self.ui.line_Ayudavta.clear()
        self.ui.line_Pedido.clear()
        self.ui.line_Otros.clear()
        self.ui.line_Tamanio.clear()
        self.ui.line_Litros.clear()
        self.ui.line_Pcio_Costo.clear()
        self.ui.line_Costo10.clear()
        self.ui.line_PSPV.clear()
        self.ui.line_Pcio_Lista.clear()
        self.ui.line_Puntos.clear()
        self.ui.line_Puntos_MG.clear()
        self.ui.textEdit_Comentarios.clear()
        self.ui.label_Imagen1.setText("SIN IMAGEN")
        self.ui.label_InfoMes.clear()
        self.LINE_ID_ACTIVO = True
        self.LINE_COD_ACTIVO  = True
        if LineLibre == 0:
            self.ui.line_ID.setFocus()

    def Carga_Img(self, Img):
        encontrado = 0
        Imagenes = self.Retorna_Imagenes()
        for i in Imagenes:
            if i == Img + ".jpg":
                encontrado = 1
                break
            if i == Img + ".png":
                encontrado = 2
                break
        
        if encontrado == 1:
            Imagen = "./img\\" + Img + ".jpg"
            Imagen = QPixmap(Imagen)
            Imagen = Imagen.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.ui.label_Imagen1.setPixmap(Imagen)
        elif encontrado == 2:
            Imagen = "./img\\" + Img + ".png"
            Imagen = QPixmap(Imagen)
            Imagen = Imagen.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.ui.label_Imagen1.setPixmap(Imagen)
        elif encontrado == 0:
            self.ui.label_Imagen1.setText("SIN IMAGEN")

    def Retorna_Imagenes(self, ruta = './img'):
        return next(walk(ruta))[2]

    # Carga en la ventana los datos que pueden venir de la bd o el excel, en ambos casos se debe actualizar los datos globales. Tener en cuenta que se encarga de convertir los datos al formato que le corresponde, TENER EN CUENTA QUE ES IMPORTANTE QUE ÉSTA FUNCIÓN REALICE DICHO AJUSTE!
    # Si el parámetro "Nuevo" viene en True, es porque se utiliza ésta misma función cuando en el Excel se encuentra un producto nuevo
    def V_T_Cargar_Datos(self, Datos, Nuevo = False):
        self.LINE_ID_ACTIVO = False
        self.LINE_COD_ACTIVO = False
        self.LINE_PUNTOS_ACTIVO = False
        self.LINE_PUNTOSMG_ACTIVO = False

        self.LINEVALOR1 = fts.Formato_ValorF_Variable(Datos[13])
        self.LINEVALOR2 = fts.Formato_ValorF_Variable(Datos[14])
        self.LINEVALOR3 = fts.Formato_ValorF_Variable(Datos[15])
        self.LINEVALOR4 = fts.Formato_ValorF_Variable(Datos[16])
        Datos = self.R_T_Convierte_Datos_Para_Ventana(Datos)

        # Id
        if Nuevo == True:
            self.ui.line_ID.setText('')
        else:
            self.ui.line_ID.setText(Datos[0])            
        # Activo
        self.ui.checkBox_Activo.setChecked(Datos[1])
        if Datos[1] == False:
            self.MuestraMsjOK("Este producto está DESACTIVADO","Aviso importante!")
        # Codigo
        self.ui.line_Codigo.setText(Datos[2])
        self.ui.comboBox_Linea.setCurrentIndex(mi_vars.LINEANUM.index(Datos[3]))
        self.ui.comboBox_Tipo.setCurrentIndex(Datos[4])
        self.ui.comboBox_Interior.setCurrentIndex(Datos[5])
        self.ui.line_Repuesto.setText(Datos[6])
        self.ui.line_Bazar.setText(Datos[7])
        self.ui.line_Ayudavta.setText(Datos[8])
        self.ui.line_Pedido.setText(Datos[9])
        self.ui.line_Otros.setText(Datos[10])
        self.ui.line_Tamanio.setText(Datos[11])
        self.ui.line_Litros.setText(Datos[12])
        self.ui.line_Pcio_Costo.setText(Datos[13])
        self.ui.line_Costo10.setText(Datos[14])
        self.ui.line_PSPV.setText(Datos[15])
        self.ui.line_Pcio_Lista.setText(Datos[16])
        self.ui.line_Puntos.setText(Datos[17])
        self.ui.line_Puntos_MG.setText(Datos[18])
        self.ui.textEdit_Comentarios.setText(Datos[19])
        self.Carga_Img(Datos[2])
        self.ui.label_InfoMes.setText(Datos[21])
        self.LINE_ID_ACTIVO = True
        self.LINE_COD_ACTIVO = True
        self.LINE_PUNTOS_ACTIVO = True
        self.LINE_PUNTOSMG_ACTIVO = True
