'''
Cargar todos los datos que se puedan. Por ej, formas de pago sirve porque si es un cliente que paga en efectivo algunos productos generan ganancia directa, si tiene tarjeta
naranja tiene unas promos, si es del hipotecario otras, y así sucesivamente. Intentar implementar las formas de pago con números y una tabla, por ejemplo, 1: efectivo - 2:Visa
3: Visa-Hipotecario, etc... Así puedo tener cientos de formas de pago y en la base de datos del cliente sólo agendo un integer
'''

from PySide2.QtWidgets import QMainWindow
from vtn.vtn_clie import Ui_Cliente_BD
from vtn.cla_clie_nue import V_ClienteNuevo

class V_Clientes(QMainWindow):
    def __init__(self, VentanaAnterior):
        super(V_Clientes, self).__init__()
        self.ui = Ui_Cliente_BD()
        self.ui.setupUi(self)
        self.Ant = VentanaAnterior

        self.ui.push_Menu.clicked.connect(self.Btn_Clic_Volver)
        self.ui.push_Nuevo.clicked.connect(self.Btn_Clic_Nuevo)
    

    def Btn_Clic_Volver(self):
        self.close()


    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.Ant.show()

    def Btn_Clic_Nuevo(self):
        self.hide()
        try:
            self.ui.Ventana_Nuevo_Cliente.show()
        except:
            self.ui.Ventana_Nuevo_Cliente = V_ClienteNuevo(self)
            self.ui.Ventana_Nuevo_Cliente.show()

