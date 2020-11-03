from PySide2.QtWidgets import QDialog
from vtn.vtn_conf import Ui_Configuracion

class V_Configuracion(QDialog):
    def __init__(self, VentanaAnterior):
        super(V_Configuracion, self).__init__()
        self.ui = Ui_Configuracion()
        self.ui.setupUi(self)
        self.Ant = VentanaAnterior

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.Ant.show()