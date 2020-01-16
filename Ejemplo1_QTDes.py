from PyQt5 import QtWidgets, uic
import sys


# USAREMOS PYQT5 EN VEZ DE PYSIDE2
class Fiestra():
    def __init__(self):
        # CARGAMOS NUESTRA VENTANA DE QTDES Y USAMOS SUS COMPONENTES:
        self.ui = uic.loadUi("pruebaVentana1.ui")
        #PROBAMOS LAS SEÑALES PUESTAS DESDE QTDES, PARA ELLO COMENTAMOS ESTA
        #self.ui.btnPulsa.clicked.connect(self.on_boton_clicked)
        #HEMOS PUESTO UNA SEÑAL DE MANERA QUE AL PULSAR EL BOTÓN SE CIERRE LA VENTANA MAIN

        self.ui.show()

    def on_boton_clicked(self):
        self.ui.label1.setText("Botón Pulsado")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    aplicacion = Fiestra()
    sys.exit(app.exec())
