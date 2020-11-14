'''
GENERALES
    Ventana que se utiliza para la búsqueda de productos llamada desde cualquier parte que sea necesaria del programa.
    Cuenta con una lista de botones a la izquierda que selecciona a grandes rasgos algunos productos, y pegados a ella hacia su derecha otros 6 botones que son para la búsqueda
    de aquellas Piezas según su línea.
    Nos manejamos con los Id de cada producto, así entonces, en la lista global llamada LISTABUSCAR cargamos todos los Id buscados según lo que se haya elegido en las opciones
    de los botones. Ésta lista viene acompañada de otra a nivel global del programa guardada en el módulo interno llamado vars.py, que se encarga de guardar todas las variables
    que se necesitan a nivel global, y tiene la lista LISTABUSCADO. En ella se va creando una lista en función a lo que el usuario va eligiendo, entonces, si por ej se eligen
    5 productos, la lista carga los 5 id's y al salirse esa lista es leída por la ventana que nos llamó. Entonces por ejemplo si fuimos llamados de la ventana de Promos, en
    ese caso se cargarían los 5 productos a la lista de dicha ventana.
    Si se viene desde la ventana de "Productos", al hacer clic en un producto simplemente se vuelve a la ventana anterior con el ID de dicho producto y así se cargarían todos
    sus datos.
    Hay dos modos de trabajar, donde en el primero sería que al hacer clic en un producto directamente se cierra ésta ventana mandando un único producto a la ventana que nos
    llamó, y la otra manera sería que va cargando una lista con los datos, y cuando se presiona el botón "Cargar" se cierra y se mandan todos los datos en una la lista global
    LISTABUSCADO.
    En la 2da lista de botones de selección donde están las piezas, se cargarán aquellas líneas en orden siendo las primeras las líneas que tengan sí o sí productos activos, 
    luego serán ordenadas por su cantidad de elementos. Al final se enviarán las líneas desactivadas.
'''

from PySide2.QtWidgets import QDialog
from PySide2 import QtCore, QtGui, QtWidgets
from os import walk
from PySide2.QtGui import QPixmap, QIcon

from vtn.vtn_busc import Ui_BuscarProducto

import mod.vars as mi_vars
import mod.mdb as mdb

''' LISTABUSCAR > Es la lista completa de elementos que se buscaron. Si por ejemplo se buscaron 34 productos, la lista tiene los 34 productos a pesar de que en pantalla sólo 
    figuran de a 20 productos. Desde ahí se nutre el programa para saber qué productos hay que mostrar en pantalla.
    
    LISTABPOS > Es la lista de las posiciones que existen con colores pintados. Por ejemplo, si estamos en una lista de elementos que están mostrados en pantalla y presionamos 
    otro botón que cambia los productos mostrados, ésta lista le indica los botones que están seleccionados para saber cuáles hay que des-seleccionar. Por el contrario si la 
    lista está vacía es porque no hay nada en pantalla seleccionado. Es importante aclarar que ésta lista tiene la finalidad de tener el aviso, una bandera que indica qué está 
    seleccionado actualmente y no sirve para más nada. Además importante aclarar que cada valor en la lista representa la posición de un botón, que van del 1 al 20.

    mi_vars.LISTABUSCADO > Es una lista global que acumula todos los productos en que se tienen interés y se han buscado. Luego al abrir por ejemplo la ventana de combos, la 
    misma tiene acceso a ésta lista y carga lo que se seleccionó en ésta ventana.
'''
LISTABUSCAR = []
LISTABPOS = []

class V_Buscar(QDialog):
    def __init__(self, Ventana_Prod, Ventana_Promo):
        super(V_Buscar, self).__init__()
        self.ui = Ui_BuscarProducto()
        self.ui.setupUi(self)
        self.Prod = Ventana_Prod
        self.Prom = Ventana_Promo

        # BOTONES
        # Interacción
        self.ui.push_Cancelar.clicked.connect(self.Btn_Cancelar)
        self.ui.push_Cargar.clicked.connect(self.Btn_Cargar)
        self.ui.push_Atras.clicked.connect(self.Btn_Atras)
        self.ui.push_Adelante.clicked.connect(self.Btn_Adelante)

        # Menú Principal
        self.ui.push_Repuesto.clicked.connect(self.Btn_Repuesto)
        self.ui.push_Bazar.clicked.connect(self.Btn_Bazar)
        self.ui.push_Aventas.clicked.connect(self.Btn_Aventas)
        self.ui.push_PedidosEsp.clicked.connect(self.Btn_PedidosEsp)
        self.ui.push_Otros.clicked.connect(self.Btn_Otros)
        # Menú Secundario
        self.ui.push_op1.clicked.connect(self.Btn_op1)
        self.ui.push_op2.clicked.connect(self.Btn_op2)
        self.ui.push_op3.clicked.connect(self.Btn_op3)
        self.ui.push_op4.clicked.connect(self.Btn_op4)
        self.ui.push_op5.clicked.connect(self.Btn_op5)
        self.ui.push_op6.clicked.connect(self.Btn_op6)
        self.ui.push_op7.clicked.connect(self.Btn_op7)

        # Botones de Imagenes
        self.ui.push_1.clicked.connect(self.Boton1)
        self.ui.push_2.clicked.connect(self.Boton2)
        self.ui.push_3.clicked.connect(self.Boton3)
        self.ui.push_4.clicked.connect(self.Boton4)
        self.ui.push_5.clicked.connect(self.Boton5)
        self.ui.push_6.clicked.connect(self.Boton6)
        self.ui.push_7.clicked.connect(self.Boton7)
        self.ui.push_8.clicked.connect(self.Boton8)
        self.ui.push_9.clicked.connect(self.Boton9)
        self.ui.push_10.clicked.connect(self.Boton10)
        self.ui.push_11.clicked.connect(self.Boton11)
        self.ui.push_12.clicked.connect(self.Boton12)
        self.ui.push_13.clicked.connect(self.Boton13)
        self.ui.push_14.clicked.connect(self.Boton14)
        self.ui.push_15.clicked.connect(self.Boton15)
        self.ui.push_16.clicked.connect(self.Boton16)
        self.ui.push_17.clicked.connect(self.Boton17)
        self.ui.push_18.clicked.connect(self.Boton18)
        self.ui.push_19.clicked.connect(self.Boton19)
        self.ui.push_20.clicked.connect(self.Boton20)
       
        # Indica a los botones de Anterior y Siguiente cuál es el Inicio de la lista
        self.INICIOLISTABUSCAR = 0

        # Variable para saber si se cierra la ventana desde el botón de CARGAR, de lo contrario, no hay que llevar datos
        self.VUELVE_CARGAR = False

        # Cargamos en ésta variable el botón que se apretó, para que si se vuelve a apretar el mismo no se realice todo el proceso de carga de datos
        self.BOTON_APRETADO = -1

        self.ui.push_Atras.setEnabled(False)
        self.ui.push_Adelante.setEnabled(False)

        # 229, 229, 229
        # 236, 236, 236
        # 0, 170, 225
    
    '''########################################################################################################################################
    ###########################################################################################################################################
                                                     FUNCIONES DE LA VENTANA                                                                '''

    def showEvent(self, event):
        # Limpiamos la lista que contiene los valores buscados, aquellos que se usan en la ventana que nos llamó
        mi_vars.LISTABUSCADO = []
        # Utilizamos ésta lista vacía para que deje invisibles todos los botones y los labels
        self.Car_Img_Btn_Art(mi_vars.LISTABUSCADO)
        # Se deshabilitan los botones que sólo deben estar habilitados cuando la lista de productos supera las 20 unidades
        self.ui.push_Atras.setEnabled(False)
        self.ui.push_Adelante.setEnabled(False)
        # Actualizamos las imagenes que corresponden a la 2da cinta de botones
        self.Actualiza_Lineas()
        # Quitamos las selecciones que pudieron haber quedado de otra búsqueda
        self.Controla_Selecciones()

    def mostrar(self):
        self.show()

    def closeEvent(self, event):
        # Evitamos que se cierre el programa, ignorando el evento pero ocultando la ventana
        event.ignore()
        self.hide()
        # Cuando se cierra la ventana o se cancela la búsqueda no devolvemos nada a la ventana que nos llamó, por eso limpiamos LISTABUSCADO
        if self.VUELVE_CARGAR == False:
            mi_vars.LISTABUSCADO = []
        
        if mi_vars.ORIGEN_BUSCAR == 2:
            # Le indicamos a la ventana que se está por abrir, que acaba de volver desde la ventana "Buscar"
            mi_vars.ORIGEN_BUSCAR = 1
            self.Prom.show()
        if mi_vars.ORIGEN_BUSCAR == 3:
            # Le indicamos a la ventana que se está por abrir, que acaba de volver desde la ventana "Buscar"
            mi_vars.ORIGEN_BUSCAR = 1
            self.Prod.show()
        if mi_vars.ORIGEN_BUSCAR == 4:
            # Le indicamos a la ventana que se está por abrir, que acaba de volver desde la ventana "Buscar"
            mi_vars.ORIGEN_BUSCAR = 1
            self.Vent_ClieNu.show()

    # Actualizamos las imagenes que hay en la 2da cinta de botones, donde están las líneas de las piezas.
        # Esto es así, porque las líneas puede sufrir modificaciones en el orden que tienen, porque por ejemplo, primero se colocan las líneas
        # que tienen al menos un elemento activo y luego se colocan las inactivas.
    def Actualiza_Lineas(self):

        # VARIABLES
        # Cargamos la lista de imagenes que tiene la carpeta
        Imagenes = next(walk("./icon\\TITULOS\\"))[2]
        Ancho = 100
        Alto = 100
        # En listaPos vamos a colocar la imagen, y si no se encuentra un "False". De esa forma cuando una imagen no exista lo que hacemos es mostrar el texto correspondiente.
        ListaPos = []
        Lista = []
        Cont = 1

        # Rastreamos las 6 imagenes que existan en la carpeta TITULOS y las cargamos, de lo contrario dejamos False
        while Cont < 7:
            encontrado = False
            Registro = mdb.Reg_Un_param(mi_vars.BaseDeDatos, "Linea", "Orden", Cont)
            for pos in Registro:
                Buscar = pos[3]
            for i in Imagenes:
                if i == Buscar + ".jpg":
                    Lista.append(Buscar + ".jpg")
                    encontrado = True
                    break
                elif i == Buscar + ".png":
                    Lista.append(Buscar + ".png")
                    encontrado = True
                    break
            if encontrado == False:
                ListaPos.append(False)
                Lista.append(Buscar)
            else:
                ListaPos.append(Lista[Cont - 1])
            Cont += 1

        # Btn Opc 1
        if ListaPos[0] == False:
            self.ui.push_op1.setText(Lista[0])
        else:
            self.ui.push_op1.setText("")
            Imagen = QtGui.QIcon()
            Imagen.addPixmap(QtGui.QPixmap("icon\\TITULOS\\" + Lista[0]), QtGui.QIcon.Normal, QtGui.QIcon.On)
            self.ui.push_op1.setIcon(Imagen)
            self.ui.push_op1.setIconSize(QtCore.QSize(Ancho, Alto))

        # Btn Opc 2
        if ListaPos[1] == False:
            self.ui.push_op2.setText(Lista[1])
        else:
            self.ui.push_op2.setText("")
            Imagen = QtGui.QIcon()
            Imagen.addPixmap(QtGui.QPixmap("icon\\TITULOS\\" + Lista[1]), QtGui.QIcon.Normal, QtGui.QIcon.On)
            self.ui.push_op2.setIcon(Imagen)
            self.ui.push_op2.setIconSize(QtCore.QSize(Ancho, Alto))
        
        # Btn Opc 3
        if ListaPos[2] == False:
            self.ui.push_op3.setText(Lista[2])
        else:
            self.ui.push_op3.setText("")
            Imagen = QtGui.QIcon()
            Imagen.addPixmap(QtGui.QPixmap("icon\\TITULOS\\" + Lista[2]), QtGui.QIcon.Normal, QtGui.QIcon.On)
            self.ui.push_op3.setIcon(Imagen)
            self.ui.push_op3.setIconSize(QtCore.QSize(Ancho, Alto))

        # Btn Opc 4
        if ListaPos[3] == False:
            self.ui.push_op4.setText(Lista[3])
        else:
            self.ui.push_op4.setText("")
            Imagen = QtGui.QIcon()
            Imagen.addPixmap(QtGui.QPixmap("icon\\TITULOS\\" + Lista[3]), QtGui.QIcon.Normal, QtGui.QIcon.On)
            self.ui.push_op4.setIcon(Imagen)
            self.ui.push_op4.setIconSize(QtCore.QSize(Ancho, Alto))

        # Btn Opc 5
        if ListaPos[4] == False:
            self.ui.push_op5.setText(Lista[4])
        else:
            self.ui.push_op5.setText("")
            Imagen = QtGui.QIcon()
            Imagen.addPixmap(QtGui.QPixmap("icon\\TITULOS\\" + Lista[4]), QtGui.QIcon.Normal, QtGui.QIcon.On)
            self.ui.push_op5.setIcon(Imagen)
            self.ui.push_op5.setIconSize(QtCore.QSize(Ancho, Alto))

        # Btn Opc 6
        if ListaPos[5] == False:
            self.ui.push_op6.setText(Lista[5])
        else:
            self.ui.push_op6.setText("")
            Imagen = QtGui.QIcon()
            Imagen.addPixmap(QtGui.QPixmap("icon\\TITULOS\\" + Lista[5]), QtGui.QIcon.Normal, QtGui.QIcon.On)
            self.ui.push_op6.setIcon(Imagen)
            self.ui.push_op6.setIconSize(QtCore.QSize(Ancho, Alto))
        
        # Btn Opc 6 (Como sabemos que hay más de 6 líneas de piezas, directamente a la última la llamamos "OTROS")
        self.ui.push_op7.setText("")
        Imagen = QtGui.QIcon()
        Imagen.addPixmap(QtGui.QPixmap("icon\\TITULOS\\Otros.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ui.push_op7.setIcon(Imagen)
        self.ui.push_op7.setIconSize(QtCore.QSize(Ancho, Alto))

    '''########################################################################################################################################
    ###########################################################################################################################################
                                                    FUNCIONES RELATIVAS BOTONES                                                             '''

    def Btn_Repuesto(self):
        # Despinta lo seleccionado
        self.Despintamos_Todo()

        self.ui.push_Atras.setEnabled(False)
        self.ui.push_Adelante.setEnabled(False)
        global LISTABUSCAR
        LISTABUSCAR = []

        # Una vez que sabemos qué valor tiene, creamos la lista con todos los ID de productos que lo contienen
        Tabla = mdb.Dev_Tabla(mi_vars.BaseDeDatos, "Productos")
        LISTABUSCAR = []
        for reg in Tabla:
            if reg[6] != "":
                LISTABUSCAR.append(reg[0])

        # Cargamos los productos capturados en las imagenes de artículos
        if len(LISTABUSCAR) > 20:
            self.ui.push_Adelante.setEnabled(True)
        self.INICIOLISTABUSCAR = 0
        self.Car_Img_Btn_Art(LISTABUSCAR)

        self.Controla_Selecciones()
    def Btn_Bazar(self):
        # Despinta lo seleccionado
        self.Despintamos_Todo()

        self.ui.push_Atras.setEnabled(False)
        self.ui.push_Adelante.setEnabled(False)
        global LISTABUSCAR
        LISTABUSCAR = []

        # Una vez que sabemos qué valor tiene, creamos la lista con todos los ID de productos que lo contienen
        Tabla = mdb.Dev_Tabla(mi_vars.BaseDeDatos, "Productos")
        LISTABUSCAR = []
        for reg in Tabla:
            if reg[7] != "":
                LISTABUSCAR.append(reg[0])

        # Cargamos los productos capturados en las imagenes de artículos
        if len(LISTABUSCAR) > 20:
            self.ui.push_Adelante.setEnabled(True)
        self.INICIOLISTABUSCAR = 0
        self.Car_Img_Btn_Art(LISTABUSCAR)

        self.Controla_Selecciones()
    def Btn_Aventas(self):
        # Despinta lo seleccionado
        self.Despintamos_Todo()
        
        self.ui.push_Atras.setEnabled(False)
        self.ui.push_Adelante.setEnabled(False)
        global LISTABUSCAR
        LISTABUSCAR = []

        # Una vez que sabemos qué valor tiene, creamos la lista con todos los ID de productos que lo contienen
        Tabla = mdb.Dev_Tabla(mi_vars.BaseDeDatos, "Productos")
        LISTABUSCAR = []
        for reg in Tabla:
            if reg[8] != "":
                LISTABUSCAR.append(reg[0])

        # Cargamos los productos capturados en las imagenes de artículos
        if len(LISTABUSCAR) > 20:
            self.ui.push_Adelante.setEnabled(True)
        self.INICIOLISTABUSCAR = 0
        self.Car_Img_Btn_Art(LISTABUSCAR)

        self.Controla_Selecciones()
    def Btn_PedidosEsp(self):
        # Despinta lo seleccionado
        self.Despintamos_Todo()

        self.ui.push_Atras.setEnabled(False)
        self.ui.push_Adelante.setEnabled(False)
        global LISTABUSCAR
        LISTABUSCAR = []

        # Una vez que sabemos qué valor tiene, creamos la lista con todos los ID de productos que lo contienen
        Tabla = mdb.Dev_Tabla(mi_vars.BaseDeDatos, "Productos")
        LISTABUSCAR = []
        for reg in Tabla:
            if reg[9] != "":
                LISTABUSCAR.append(reg[0])

        # Cargamos los productos capturados en las imagenes de artículos
        if len(LISTABUSCAR) > 20:
            self.ui.push_Adelante.setEnabled(True)
        self.INICIOLISTABUSCAR = 0
        self.Car_Img_Btn_Art(LISTABUSCAR)

        self.Controla_Selecciones()
    def Btn_Otros(self):
        # Despinta lo seleccionado
        self.Despintamos_Todo()

        self.ui.push_Atras.setEnabled(False)
        self.ui.push_Adelante.setEnabled(False)
        global LISTABUSCAR
        LISTABUSCAR = []

        # Una vez que sabemos qué valor tiene, creamos la lista con todos los ID de productos que lo contienen
        Tabla = mdb.Dev_Tabla(mi_vars.BaseDeDatos, "Productos")
        LISTABUSCAR = []
        for reg in Tabla:
            if reg[10] != "":
                LISTABUSCAR.append(reg[0])

        # Cargamos los productos capturados en las imagenes de artículos
        if len(LISTABUSCAR) > 20:
            self.ui.push_Adelante.setEnabled(True)
        self.INICIOLISTABUSCAR = 0
        self.Car_Img_Btn_Art(LISTABUSCAR)

        self.Controla_Selecciones()
    
    def Btn_Cancelar(self):
        self.close()
    
    def Btn_Cargar(self):
        self.VUELVE_CARGAR = True
        self.close()

    def Btn_Atras(self):
        # Despinta lo seleccionado
        self.Despintamos_Todo()
        global LISTABUSCAR
        self.INICIOLISTABUSCAR -= 20
        self.Car_Img_Btn_Art(LISTABUSCAR[self.INICIOLISTABUSCAR:])
        self.ui.push_Adelante.setEnabled(True)
        if self.INICIOLISTABUSCAR == 0:
            self.ui.push_Atras.setEnabled(False)
        self.Controla_Selecciones()

    def Btn_Adelante(self):
        # Despinta lo seleccionado
        self.Despintamos_Todo()
        global LISTABUSCAR
        self.INICIOLISTABUSCAR += 20
        self.Car_Img_Btn_Art(LISTABUSCAR[self.INICIOLISTABUSCAR:])
        self.ui.push_Atras.setEnabled(True)
        Largo = len(LISTABUSCAR)
        if self.INICIOLISTABUSCAR + 20  > Largo:
            self.ui.push_Adelante.setEnabled(False)
        self.Controla_Selecciones()

    # Botones de Opción Secundarios
        # La posición corresponde a la ubicación que hay dentro de la base de datos. Es decir, que dentro de la misma la posición 1 = - (guión), y las posiciones de las LÍNEAS comienzan desde el número 2, por ello es que se llama a la función con el primer botón valor 2, porque va a representar la primer posición de la tabla "Linea"
    def Btn_op1(self):
        self.Opciones_LINEA(1)
    def Btn_op2(self):
        self.Opciones_LINEA(2)
    def Btn_op3(self):
        self.Opciones_LINEA(3)
    def Btn_op4(self):
        self.Opciones_LINEA(4)
    def Btn_op5(self):
        self.Opciones_LINEA(5)
    def Btn_op6(self):
        self.Opciones_LINEA(6)
    def Btn_op7(self):
        self.Opciones_LINEA(7)

    # Cuando se presionó el Botón 1 para buscar las piezas, los botones de opciones se cargaron con las opciones de LINEA. Ahora se debe interpretar sus valores
    def Opciones_LINEA(self, Posicion):
        global LISTABUSCAR

        # Despinta lo seleccionado
        self.Despintamos_Todo()
        self.ui.push_Atras.setEnabled(False)
        self.ui.push_Adelante.setEnabled(False)
                
        # Evitamos que si ya se ha apretado antes un botón, no vuelva a ejecutarse la misma tarea
        if self.BOTON_APRETADO != Posicion:
            
            self.BOTON_APRETADO = Posicion
            LISTABUSCAR = []
            
            if Posicion == 7:
                # Ahora necesito tener una lista de las líneas que van en "Otros", pero como las que le preceden en los 6 botones anteriores no tienen orden, es decir que la última línea puede tener la posición 1 y así sucesivamente, lo que vamos a hacer es guardar el valor de las 6 líneas cargadas, es decir, que vamos a hacer lo contrario capturando los valores de las líneas que sí están. Entonces, después puedo asegurarme de buscar la "no coincidencia" en caso de que se haya apretado "Otros"
                AuxListaLinea = []
                for pos in range(7):
                    AuxListaLinea.append(mi_vars.LINEANUM[pos])
            else:
                # Agendamos el valor de la Linea que se está buscando
                AuxLinea = mi_vars.LINEANUM[Posicion]
            
            # Traemos la tabla de productos entera
            Tabla = mdb.Dev_Tabla(mi_vars.BaseDeDatos, "Productos")

            if Posicion == 7:
                for reg in Tabla:
                    if reg[3] != 0:
                        try:
                            AuxListaLinea.index(reg[3])
                        except:
                            LISTABUSCAR.append(reg[0])
            else:
                for reg in Tabla:
                    if reg[3] == AuxLinea:
                        LISTABUSCAR.append(reg[0])       

            # Cargamos los productos capturados en las imagenes de artículos
            if len(LISTABUSCAR) > 20:
                self.ui.push_Adelante.setEnabled(True)
            self.INICIOLISTABUSCAR = 0
            self.Car_Img_Btn_Art(LISTABUSCAR)

            self.Controla_Selecciones()

    def Boton1(self):
        self.Pinta_Seleccion(1)
        self.Interaccion_Boton(1)
    def Boton2(self):
        self.Pinta_Seleccion(2)
        self.Interaccion_Boton(2)
    def Boton3(self):
        self.Pinta_Seleccion(3)
        self.Interaccion_Boton(3)
    def Boton4(self):
        self.Pinta_Seleccion(4)
        self.Interaccion_Boton(4)
    def Boton5(self):
        self.Pinta_Seleccion(5)
        self.Interaccion_Boton(5)
    def Boton6(self):
        self.Pinta_Seleccion(6)
        self.Interaccion_Boton(6)
    def Boton7(self):
        self.Pinta_Seleccion(7)
        self.Interaccion_Boton(7)
    def Boton8(self):
        self.Pinta_Seleccion(8)
        self.Interaccion_Boton(8)
    def Boton9(self):
        self.Pinta_Seleccion(9)
        self.Interaccion_Boton(9)
    def Boton10(self):
        self.Pinta_Seleccion(10)
        self.Interaccion_Boton(10)
    def Boton11(self):
        self.Pinta_Seleccion(11)
        self.Interaccion_Boton(11)
    def Boton12(self):
        self.Pinta_Seleccion(12)
        self.Interaccion_Boton(12)
    def Boton13(self):
        self.Pinta_Seleccion(13)
        self.Interaccion_Boton(13)
    def Boton14(self):
        self.Pinta_Seleccion(14)
        self.Interaccion_Boton(14)
    def Boton15(self):
        self.Pinta_Seleccion(15)
        self.Interaccion_Boton(15)
    def Boton16(self):
        self.Pinta_Seleccion(16)
        self.Interaccion_Boton(16)
    def Boton17(self):
        self.Pinta_Seleccion(17)
        self.Interaccion_Boton(17)
    def Boton18(self):
        self.Pinta_Seleccion(18)
        self.Interaccion_Boton(18)
    def Boton19(self):
        self.Pinta_Seleccion(19)
        self.Interaccion_Boton(19)
    def Boton20(self):
        self.Pinta_Seleccion(20)
        self.Interaccion_Boton(20)
    # Los 20 botones de arriba corresponden a la lista de productos. Hay 2 formas de trabajar, dependiendo desde donde es llamado puede que se seleccione un producto o varios.
        # Si se selecciona 1 como por ejemplo la ventana "Productos" que es para ver y editar los detalles de cada producto individualmente, donde no pueden verse ni compararse
        # mas productos al mismo tiempo, en esos casos al hacer clic en uno de los 20 botones, automáticamente nos se cierra y nos lleva a la ventana. Pero si se necesitan 
        # seleccionar más productos como en las promos, se crea una lista y sólo nos retiramos cuando se presiona el botón de "Cargar"
    def Interaccion_Boton(self, Numero):
        global LISTABUSCAR
        # 2: Estamos en la ventana "Buscar" y viene desde "Promos", se crea una lista con los ID de cada prod seleccionado
        if mi_vars.ORIGEN_BUSCAR == 2 or mi_vars.ORIGEN_BUSCAR == 4:
            ID_Agregar = LISTABUSCAR[Numero - 1 + self.INICIOLISTABUSCAR]
            Aux = 0
            try:
                Aux = mi_vars.LISTABUSCADO.index(ID_Agregar)
                mi_vars.LISTABUSCADO.pop(Aux)
                self.Despinta_Seleccion(Numero)
            except:
                mi_vars.LISTABUSCADO.append(ID_Agregar)

        # 3: Estamos en la ventana "Buscar" y viene desde "Productos"
        elif mi_vars.ORIGEN_BUSCAR == 3:
            self.VUELVE_CARGAR = True
            mi_vars.LISTABUSCADO = []
            mi_vars.LISTABUSCADO.append(LISTABUSCAR[Numero - 1 + self.INICIOLISTABUSCAR])
            self.Despinta_Seleccion(Numero)
            self.close()
    
    '''########################################################################################################################################
    ###########################################################################################################################################
                                                                    FUNCIONES                                                                '''
    
    # PINTA de color NARANJA al botón que tenga que estar seleccionado
    def Pinta_Seleccion(self, Numero):
        global LISTABPOS
        if Numero > 0:
            if Numero == 1:
                self.ui.push_1.setStyleSheet("background-color: rgb(237, 127, 16);")
            elif Numero == 2:
                self.ui.push_2.setStyleSheet("background-color: rgb(237, 127, 16);")
            elif Numero == 3:
                self.ui.push_3.setStyleSheet("background-color: rgb(237, 127, 16);")
            elif Numero == 4:
                self.ui.push_4.setStyleSheet("background-color: rgb(237, 127, 16);")
            elif Numero == 5:
                self.ui.push_5.setStyleSheet("background-color: rgb(237, 127, 16);")
            elif Numero == 6:
                self.ui.push_6.setStyleSheet("background-color: rgb(237, 127, 16);")
            elif Numero == 7:
                self.ui.push_7.setStyleSheet("background-color: rgb(237, 127, 16);")
            elif Numero == 8:
                self.ui.push_8.setStyleSheet("background-color: rgb(237, 127, 16);")
            elif Numero == 9:
                self.ui.push_9.setStyleSheet("background-color: rgb(237, 127, 16);")
            elif Numero == 10:
                self.ui.push_10.setStyleSheet("background-color: rgb(237, 127, 16);")
            elif Numero == 11:
                self.ui.push_11.setStyleSheet("background-color: rgb(237, 127, 16);")
            elif Numero == 12:
                self.ui.push_12.setStyleSheet("background-color: rgb(237, 127, 16);")
            elif Numero == 13:
                self.ui.push_13.setStyleSheet("background-color: rgb(237, 127, 16);")
            elif Numero == 14:
                self.ui.push_14.setStyleSheet("background-color: rgb(237, 127, 16);")
            elif Numero == 15:
                self.ui.push_15.setStyleSheet("background-color: rgb(237, 127, 16);")
            elif Numero == 16:
                self.ui.push_16.setStyleSheet("background-color: rgb(237, 127, 16);")
            elif Numero == 17:
                self.ui.push_17.setStyleSheet("background-color: rgb(237, 127, 16);")
            elif Numero == 18:
                self.ui.push_18.setStyleSheet("background-color: rgb(237, 127, 16);")
            elif Numero == 19:
                self.ui.push_19.setStyleSheet("background-color: rgb(237, 127, 16);")
            elif Numero == 20:
                self.ui.push_20.setStyleSheet("background-color: rgb(237, 127, 16);")
            LISTABPOS.append(Numero)

    # PINTA de color GRIS al botón que deja de estar seleccionado o a todos, según corresponda
        # Si el Valor Numero = 0 es porque a hay que despintar todo
    def Despinta_Seleccion(self, Numero):
        global LISTABPOS
        if Numero > 0:
            if Numero == 1:
                self.ui.push_1.setStyleSheet("background-color: rgb(236, 236, 236);")
            elif Numero == 2:
                self.ui.push_2.setStyleSheet("background-color: rgb(236, 236, 236);")
            elif Numero == 3:
                self.ui.push_3.setStyleSheet("background-color: rgb(236, 236, 236);")
            elif Numero == 4:
                self.ui.push_4.setStyleSheet("background-color: rgb(236, 236, 236);")
            elif Numero == 5:
                self.ui.push_5.setStyleSheet("background-color: rgb(236, 236, 236);")
            elif Numero == 6:
                self.ui.push_6.setStyleSheet("background-color: rgb(236, 236, 236);")
            elif Numero == 7:
                self.ui.push_7.setStyleSheet("background-color: rgb(236, 236, 236);")
            elif Numero == 8:
                self.ui.push_8.setStyleSheet("background-color: rgb(236, 236, 236);")
            elif Numero == 9:
                self.ui.push_9.setStyleSheet("background-color: rgb(236, 236, 236);")
            elif Numero == 10:
                self.ui.push_10.setStyleSheet("background-color: rgb(236, 236, 236);")
            elif Numero == 11:
                self.ui.push_11.setStyleSheet("background-color: rgb(236, 236, 236);")
            elif Numero == 12:
                self.ui.push_12.setStyleSheet("background-color: rgb(236, 236, 236);")
            elif Numero == 13:
                self.ui.push_13.setStyleSheet("background-color: rgb(236, 236, 236);")
            elif Numero == 14:
                self.ui.push_14.setStyleSheet("background-color: rgb(236, 236, 236);")
            elif Numero == 15:
                self.ui.push_15.setStyleSheet("background-color: rgb(236, 236, 236);")
            elif Numero == 16:
                self.ui.push_16.setStyleSheet("background-color: rgb(236, 236, 236);")
            elif Numero == 17:
                self.ui.push_17.setStyleSheet("background-color: rgb(236, 236, 236);")
            elif Numero == 18:
                self.ui.push_18.setStyleSheet("background-color: rgb(236, 236, 236);")
            elif Numero == 19:
                self.ui.push_19.setStyleSheet("background-color: rgb(236, 236, 236);")
            elif Numero == 20:
                self.ui.push_20.setStyleSheet("background-color: rgb(236, 236, 236);")
            aux = LISTABPOS.index(Numero)
            LISTABPOS.pop(aux)

    # Para facilitar el código, voy a despintar cada vez que se cambian los datos en cada botón, y luego se pintarán si es necesario. Esto facilita mucho el código y además no
        # es mucho trabajo ya que por lo general por cada pantalla no se seleccionan muchos elementos.
    def Despintamos_Todo(self):
        global LISTABPOS
        Tope = len(LISTABPOS)
        Cont = 0
        while Cont < Tope:
            self.Despinta_Seleccion(LISTABPOS[0])
            Cont += 1
        LISTABPOS = []

    # Función que despinta todo lo seleccionado, luego pinta aquello que sea necesario.
    def Controla_Selecciones(self):
        global LISTABUSCAR

        # Pintamos si hay algo que deba estar seleccionado
        Largo = len(mi_vars.LISTABUSCADO)
        if len(LISTABUSCAR) > 0 and Largo > 0:
            Cont = 0
            while Cont < Largo:
                try:
                    Aux = LISTABUSCAR.index(mi_vars.LISTABUSCADO[Cont])
                    if Aux >= self.INICIOLISTABUSCAR and Aux < self.INICIOLISTABUSCAR + 20:
                        self.Pinta_Seleccion(Aux + 1)
                except:
                    pass
                Cont += 1



    # Llega una lista de números ID y se cargan sus imagenes y descripción en la ventana
    def Car_Img_Btn_Art(self, Lista):
        Total = len(Lista)
        Contador = 0
        Ancho = 130
        Alto = 125

        Imagen = []
        Descripcion = []
        Activo = []



        # Con éste while recorremos la Lista y generamos 2 listas más, donde en Imagen colocamos el nombre de la imagen que corresponde por orden y en Descripción lo suyo.
        while Contador < Total:
            Auxiliar = self.R_T_Retorna_Datos_De_BBDD(ID = Lista[Contador])
            Imagen.append("./img_bus\\" + Auxiliar[2])
            if Auxiliar[3] > 0:
                Descripcion.append(Auxiliar[11] + " cm " + mi_vars.INTERIOR[Auxiliar[5]])
            else:
                Descripcion.append(Auxiliar[6] + Auxiliar[7] + Auxiliar[8] + Auxiliar[9] + Auxiliar[10])
            if Auxiliar[1] != 1:
                Activo.append(True)
            else:
                Activo.append(False)
            Contador += 1

        # Este código puede ejecutarse aún cuando no hay selección, así que vamos a evitarlo de ser necesario
        if Total <= 0:
            self.BOTON_APRETADO = 0
            self.ui.push_1.setVisible(False)
            self.ui.push_2.setVisible(False)
            self.ui.push_3.setVisible(False)
            self.ui.push_4.setVisible(False)
            self.ui.push_5.setVisible(False)
            self.ui.push_6.setVisible(False)
            self.ui.push_7.setVisible(False)
            self.ui.push_8.setVisible(False)
            self.ui.push_9.setVisible(False)
            self.ui.push_10.setVisible(False)
            self.ui.push_11.setVisible(False)
            self.ui.push_12.setVisible(False)
            self.ui.push_13.setVisible(False)
            self.ui.push_14.setVisible(False)
            self.ui.push_15.setVisible(False)
            self.ui.push_16.setVisible(False)
            self.ui.push_17.setVisible(False)
            self.ui.push_18.setVisible(False)
            self.ui.push_19.setVisible(False)
            self.ui.push_20.setVisible(False)
            self.ui.label_1.setVisible(False)
            self.ui.label_2.setVisible(False)
            self.ui.label_3.setVisible(False)
            self.ui.label_4.setVisible(False)
            self.ui.label_5.setVisible(False)
            self.ui.label_6.setVisible(False)
            self.ui.label_7.setVisible(False)
            self.ui.label_8.setVisible(False)
            self.ui.label_9.setVisible(False)
            self.ui.label_10.setVisible(False)
            self.ui.label_11.setVisible(False)
            self.ui.label_12.setVisible(False)
            self.ui.label_13.setVisible(False)
            self.ui.label_14.setVisible(False)
            self.ui.label_15.setVisible(False)
            self.ui.label_16.setVisible(False)
            self.ui.label_17.setVisible(False)
            self.ui.label_18.setVisible(False)
            self.ui.label_19.setVisible(False)
            self.ui.label_20.setVisible(False)
        else:
            # Recorremos todos los botones y les actualizamos sus imagenes
            ListaRepasados = []
            for push in self.findChildren(QtWidgets.QPushButton):
                nombre = str(push.objectName())
                valido = False
                try:
                    NumP = int(nombre[5:])
                    valido = True
                except:
                    valido = False
                if valido == True:
                    try:
                        aux = ListaRepasados.index(NumP)
                    except:
                        ListaRepasados.append(NumP)
                        if Total >= NumP:
                            push.setVisible(True)
                            icon = QtGui.QIcon()
                            icon.addPixmap(QtGui.QPixmap("./img_bus\\SinImagen.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
                            push.setIcon(icon)
                            icon.addPixmap(QtGui.QPixmap(Imagen[NumP - 1]), QtGui.QIcon.Normal, QtGui.QIcon.On)
                            push.setIcon(icon)
                            push.setIconSize(QtCore.QSize(Ancho, Alto))
                        else:
                            icon = QtGui.QIcon()
                            icon.addPixmap(QtGui.QPixmap("./img_bus\\SinImagen.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
                            push.setIcon(icon)
                            push.setVisible(False)
            
            # Recorremos todos los labels y les cargamos sus descripciones
            ListaRepasados = []
            for label in self.findChildren(QtWidgets.QLabel):
                nombre = str(label.objectName())
                valido = False
                try:
                    NumP = int(nombre[6:])
                    valido = True
                except:
                    valido = False
                if valido == True:
                    try:
                        aux = ListaRepasados.index(NumP)
                    except:
                        ListaRepasados.append(NumP)
                        if Total >= NumP:
                            label.setVisible(True)
                            label.setText(Descripcion[NumP - 1])
                            if Activo[NumP - 1] == True:
                                label.setStyleSheet("background-color: rgb(255, 170, 127);")
                            else:
                                label.setStyleSheet("background-color: rgb(236, 236, 236);")
                        else:
                            label.setVisible(False)

    # Cuando se necesitan los datos de la BBDD aquí los obtenemos ya sea según su ID o código y los retorna.
        # Si hubo error en los datos que llegaron como parámetro la posición cero tendrá un cero en formato string. Y tendrá un '1' (string) si no pudo encontrar los datos.
    def R_T_Retorna_Datos_De_BBDD(self, ID = 0, Codigo = 0):
        Datos = ['0','','','','','','','','','','','','','','','','','','']
        if (ID != 0 and Codigo != 0) or (ID == 0 and Codigo == 0):
            print("[ERROR INTERNO 887]")
        else:
            if ID != 0:
                fila = mdb.Reg_Un_param(mi_vars.BaseDeDatos,'Productos', "ID", ID)
            else:
                fila = mdb.Reg_Un_param(mi_vars.BaseDeDatos,'Productos', "Codigo", Codigo)
                
            for pos in fila:
                Datos = [pos[0],pos[1],pos[2],pos[3],pos[4],pos[5],pos[6],pos[7],pos[8],pos[9],pos[10],pos[11],pos[12],pos[13],pos[14],pos[15],pos[16],pos[17],pos[18]]
            if Datos[0] == '0':
                Datos[0] = '1'
            else:
                # A imagenes les colocamos sólo el nombre de código
                Datos[17] = str(Datos[2])
        return Datos
        # ======================= FUNCIONES ============================
    
    
