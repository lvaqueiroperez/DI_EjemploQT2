from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
import sys

datos = {'Col1': [1, 2, 3, 4],
        'Col2': [1, 3, 5, 7],
        'Col3': [1, 2, 4, 6]}


class ExemploTaboa(QTableWidget):
    def __init__(self, datos, *args):
        QTableWidget.__init__(self, *args)
        self.datos = datos
        self.asignarDatos()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def asignarDatos(self):
        cabeceirasHor = []
        for n, clave in enumerate(self.datos.keys()):
            cabeceirasHor.append(clave)
            for m, numero in enumerate(self.datos[clave]):
                novoElemento = QTableWidgetItem(str(numero))
                self.setItem(m, n, novoElemento)
        self.setHorizontalHeaderLabels(cabeceirasHor)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    taboa = ExemploTaboa(datos, 4, 3)
    taboa.show()
    sys.exit(app.exec_())