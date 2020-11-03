from PySide2.QtWidgets import QDialog
from vtn.vtn_stoc import Ui_Stockinterno

class V_Stock(QDialog):
    def __init__(self, VentanaAnterior):
        super(V_Stock, self).__init__()
        self.ui = Ui_Stockinterno()
        self.ui.setupUi(self)
        self.Ant = VentanaAnterior

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.Ant.show()