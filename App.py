'''
Los nombres de las funciones corresponden a una nomenclatura fija para un rápido entendimiento.
    Todas las funciones comienzan con su tarea general, que es explicar si retornan datos o sólo realizan acciones, es decir, si son del tipo void
    o si retornan algún dato, por ende comienzan con una "V" o "R". Luego se explica si su función Continúa con el llamado a una función o bien
    su actividad termina en ella con "C" o "T". Ahora bien, si dicha función llama a otras funciones para seguir operando ya sea porque necesita datos
    o algo adicional, significa que la función termina ahí, pero si llama a otra función que realiza alguna actividad de relevancia entonces podemos
    decir que la función continúa.

    TAREAS A REALIZAR:
    * Necesito una ventana que edite los detalles menores como los tipos de elementos que hay (ollas, sartenes, biferas, etc), interiores, etc...
    * Ver porque en BBDD productos las líneas arrancan en 1, cuando en la tabla linea arranca en 2. Es decir, marsala en Productos vale 1 y en la tabla
        Linea vale 2.
    * Revisar todo y comentar bien las funciones y su trabajo. La Clase de la ventana Productos creo que es la única bien comentada.
    PRODUCTOS:
    HACER:
        - Controlar todos los llamados que hay que hacer para controlar los cambios antes de modificar la pantalla.
        - Que Controle desde base de datos a datos obtenidos del excel, la posibilidad de que algún producto deje de estar activo.
        - Que lea cualquier archivo excel.
        - Que sepa interpretar lo que lee de un excel para cargar lo mas fielmente posible los datos como LINEA, TIPO, INTERIOR, TAMAÑO, LITROS.
            - Y si cumplo con el punto anterior, entonces tmb tengo que controlar que ésto no se haya modificado cuando aparece un excel nuevo, porque ignora todas eas cosas.
        - Probar que pasa si intenta abrir los otros formatos de excel que hay, porque quizás no funciona ésto con todos los formatos.

    VTNA CONFIG:
    * Se tiene que poder configurar la forma en que se ve la fecha de actualización en la vtna prod, porque hoy es importante el mes pero puede llegar
        a ser necesario un día transformarlo a días.

    BBDD LINEAS:
        En la base de datos, la tabla Lineas contiene cada línea de Essen. Si bien en su momento se fueron creando de manera ordenada, no responden a
        un orden específico. Conforme pase el tiempo su orden para ser mostrado al usuario irá cambiando a fin de ir ocultando aquellas LINEAS que están
        desactivadas o bien, que tienen muy poco movimiento. Esto es necesario por 2 motivos, primero que resulta más práctico tener a mano las líneas
        más buscadas, y segundo que en el buscador estamos limitados a 6 botones para las líneas, cuando la cantidad de elemntos lo supera agrupamos
        desde la posición 6 en adelante, a todos sus productos en uno sólo. Entonces es necesario tener en los 5 primeros, aquellas líneas que se usan
        más, y en las demás agruparlos en el último.
        Para solucionar ésto tenemos una columna llamada "Orden" que se ennumera para dicha acción. La misma puede ir cambiando su orden mediante
        funciones que analizen la actividad y luego plasmarlo en el mismo, teniendo en cuenta las líneas que poseen más productos y el uso que le damos
        a las mismas.
'''

'''
    HACER AHORA:
    * Quitar la navegación entre ventanas y traerlas al archivo App.py
    * Que no active más los productos por su cuenta cuando carga un excel, ahora se realizarán manualmente
    * Crear que la forma de activar productos lo haga de manera automática
'''

import time
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QSplashScreen
from PySide2.QtWidgets import QMainWindow, QMessageBox
import sys
from PySide2.QtGui import QPixmap

#import subprocess

# VENTANA PRINCIPAL: MENÚ
from vtn.vtn_menu import Ui_MainWindow

# VENTANAS SECUNDARIAS
from vtn.cla_prod import V_Productos
from vtn.cla_prom import V_Promos
#from vtn.cla_pedi import V_Pedidos
from vtn.cla_vent import V_Ventas
from vtn.cla_clie import V_Clientes
from vtn.cla_clie_nue import V_ClienteNuevo
from vtn.cla_stoc import V_Stock
#from vtn.cla_reco import V_Recordatorio
#from vtn.cla_esta import V_Estado
from vtn.cla_conf import V_Configuracion
from vtn.cla_busc import V_Buscar

# MODULOS INTERNOS
import mod.glob_func as gf
import mod.vars as mi_vars

class V_Menu(QMainWindow):
    def __init__(self):
        super(V_Menu, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.Vent_Produc = V_Productos()
        self.Vent_Promos = V_Promos(self)
        #self.Vent_Pedido = V_Pedidos(self)
        self.Vent_Ventas = V_Ventas(self)
        self.Vent_Client = V_Clientes()
        self.Vent_ClieNu = V_ClienteNuevo(self)
        self.Vent_Stock = V_Stock(self)
        #self.Vent_Record = V_Recordatorio(self)
        #self.Vent_Estado = V_Estado(self)
        self.Vent_Config = V_Configuracion(self)
        self.Vent_Buscar = V_Buscar(self.Vent_Produc, self.Vent_Promos)

        # Botones
        self.ui.push_Producto.clicked.connect(self.Abrir_Prod)
        self.ui.push_Ofertas.clicked.connect(self.Abrir_Prom)
        #self.ui.push_Pedidos.clicked.connect(self.Abrir_Pedi)
        self.ui.push_Ventas.clicked.connect(self.Abrir_Vent)
        self.ui.push_Clientes.clicked.connect(self.Abrir_Clie)
        self.ui.push_Stock.clicked.connect(self.Abrir_Stoc)
        #self.ui.push_Recordatorio.clicked.connect(self.Abrir_Reco)
        #self.ui.push_Estado.clicked.connect(self.Abrir_Esta)
        self.ui.push_Configuracion.clicked.connect(self.Abrir_Conf)

        # Botones que abren la ventana de BUSCAR desde otras ventanas
        self.Vent_Promos.ui.push_Bproduc.clicked.connect(self.Abrir_Buscar_Prom)
        self.Vent_Produc.ui.push_Buscar.clicked.connect(self.Abrir_Buscar_Prod)
        self.Vent_ClieNu.ui.push_Agrega_Deseo.clicked.connect(self.Abrir_Buscar_Clie)

        # Botones que vuelven al menú
        self.Vent_Produc.ui.push_Menu.clicked.connect(self.Abrir_Menu_Prod)
        self.Vent_Client.ui.push_Menu.clicked.connect(self.Abrir_Menu_Clientes)

        # VARIABLES
        # Para los productos
        gf.Act_Listas_Globales()

        #subprocess.Popen("D:\Programación\Python\Proyectos\Essen PySide2 - copia\Bots.py")
        
    # ======================= FUNCIONES ============================
    # Función que abre la ventana BUSCAR desde Promos
    def Abrir_Buscar_Prom(self):
        mi_vars.ORIGEN_BUSCAR = 2
        self.Vent_Promos.hide()
        self.Vent_Buscar.show()

    # Función que abre la ventana BUSCAR desde Productos
    def Abrir_Buscar_Prod(self):
        mi_vars.ORIGEN_BUSCAR = 3
        self.Vent_Produc.hide()
        self.Vent_Buscar.show()

    # Función que abre el MENÚ desde PRODUCTOS
    def Abrir_Menu_Prod(self):
        valor = self.Vent_Produc.CerrarProd()
        if valor == 0:
            ui.show()

    # Función que abre la ventana BUSCAR desde Cliente Nuevo
    def Abrir_Buscar_Clie(self):
        mi_vars.ORIGEN_BUSCAR = 4
        self.Vent_ClieNu.hide()
        self.Vent_Buscar.show()

    # Función que abre menú
    def Abrir_Menu_Clientes(self):
        self.Vent_Client.hide()
        ui.show()

    def Abrir_Prod(self):
        self.hide()
        self.Vent_Produc.mostrar()

    def Abrir_Prom(self):
        self.hide()
        self.Vent_Promos.show()

    '''
    def Abrir_Pedi(self):
        self.hide()
        self.Vent_Pedido.show()
    '''

    def Abrir_Vent(self):
        self.hide()
        self.Vent_Ventas.show()
    
    def Abrir_Clie(self):
        self.hide()
        self.Vent_Client.show()

    def Abrir_Stoc(self):
        self.hide()
        self.Vent_Stock.show()
    
    '''
    def Abrir_Reco(self):
        self.hide()
        self.Vent_Record.show()

    def Abrir_Esta(self):
        self.hide()
        self.Vent_Estado.show()
    '''

    def Abrir_Conf(self):
        self.hide()
        self.Vent_Config.show()

    def closeEvent(self, event):
        close = QMessageBox.question(self, "Salir", "¿Estás seguro/a que desea cerrar el programa?", QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    


# ================================================================
if __name__ == '__main__':
    
    aplicacion = QApplication(sys.argv)

    splash = QSplashScreen(QPixmap('./splashscreen_background.jpg'))
        # By default, SplashScreen will be in the center of the screen.
        # You can move it to a specific location if you want:
        # self.splash.move(10,10)
    splash.show()

    ui = V_Menu()
    ui.show()
    splash.finish(ui)
    sys.exit(aplicacion.exec_())