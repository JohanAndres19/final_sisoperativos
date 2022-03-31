import sys
from PyQt5.QtWidgets import *
from qt_for_python.uic.ventana import *
from Logica import *
class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.modelo=CPU()
        self.ui.pushButton.clicked.connect(lambda: self.modelo.Ejecutar())


if __name__ =="__main__":
    app =QApplication(sys.argv)
    gui = Ventana()
    gui.show()
    sys.exit(app.exec_())

