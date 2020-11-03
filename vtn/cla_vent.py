from PySide2.QtWidgets import QDialog
from vtn.vtn_vent import Ui_VentasBD

class V_Ventas(QDialog):
    def __init__(self, VentanaAnterior):
        super(V_Ventas, self).__init__()
        self.ui = Ui_VentasBD()
        self.ui.setupUi(self)
        self.Ant = VentanaAnterior

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.Ant.show()