from PySide2.QtWidgets import QMainWindow, QMessageBox
from vtn.vtn_menu import Ui_MainWindow

# VENTANAS
from vtn.cla_prod import V_Productos
from vtn.cla_prom import V_Promos
#from vtn.cla_pedi import V_Pedidos
from vtn.cla_vent import V_Ventas
from vtn.cla_clie import V_Clientes
from vtn.cla_stoc import V_Stock
#from vtn.cla_reco import V_Recordatorio
#from vtn.cla_esta import V_Estado
from vtn.cla_conf import V_Configuracion

# MODULOS INTERNOS
import mod.glob_func as gf
import mod.vars as mi_vars

class V_Menu(QMainWindow):
    def __init__(self, parent=None):
        super(V_Menu, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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

        # VARIABLES
        # Para los productos
        gf.Act_Listas_Globales()
        
    # ======================= FUNCIONES ============================
    def Abrir_Prod(self):
        self.hide()
        try:
            self.ui.Ventana_Productos.show()
        except:
            self.ui.Ventana_Productos = V_Productos(self)
            self.ui.Ventana_Productos.show()

    def Abrir_Prom(self):
        self.hide()
        try:
            self.ui.Ventana_Promociones.show()
        except:
            self.ui.Ventana_Promociones = V_Promos(self)
            self.ui.Ventana_Promociones.show()

    '''
    def Abrir_Pedi(self):
        self.hide()
        try:
            self.ui.Ventana_Pedidos.show()
        except:
            self.ui.Ventana_Pedidos = V_Promos(self)
            self.ui.Ventana_Pedidos.show()
    '''

    def Abrir_Vent(self):
        self.hide()
        try:
            self.ui.Ventana_Ventas.show()
        except:
            self.ui.Ventana_Ventas = V_Promos(self)
            self.ui.Ventana_Ventas.show()
    
    def Abrir_Clie(self):
        self.hide()
        try:
            self.ui.Ventana_Clientes.show()
        except:
            self.ui.Ventana_Clientes = V_Clientes(self)
            self.ui.Ventana_Clientes.show()

    def Abrir_Stoc(self):
        self.hide()
        try:
            self.ui.Ventana_StockInterno.show()
        except:
            self.ui.Ventana_StockInterno = V_Promos(self)
            self.ui.Ventana_StockInterno.show()
    
    '''
    def Abrir_Reco(self):
        self.hide()
        try:
            self.ui.Ventana_Recordatorios.show()
        except:
            self.ui.Ventana_Recordatorios = V_Promos(self)
            self.ui.Ventana_Recordatorios.show()

    def Abrir_Esta(self):
        self.hide()
        try:
            self.ui.Ventana_Estado.show()
        except:
            self.ui.Ventana_Estado = V_Promos(self)
            self.ui.Ventana_Estado.show()
    '''

    def Abrir_Conf(self):
        self.hide()
        try:
            self.ui.Ventana_Configuracion.show()
        except:
            self.ui.Ventana_Configuracion = V_Promos(self)
            self.ui.Ventana_Configuracion.show()




    def closeEvent(self, event):
        close = QMessageBox.question(self, "Salir", "¿Estás seguro/a que desea cerrar el programa?", QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()