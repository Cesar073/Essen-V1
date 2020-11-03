from PySide2.QtWidgets import QDialog
from vtn.vtn_fich import Ui_Ficha_Pers

class V_Ficha(QDialog):
    def __init__(self, VentanaAnterior):
        super(V_Ficha, self).__init__()
        self.ui = Ui_Ficha_Pers()
        self.ui.setupUi(self)
        self.Ant = VentanaAnterior

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.Ant.show()