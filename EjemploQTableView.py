from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
import sys

#EJEMPLO DE USO DE UN "QTableView"

#CREAMOS UNA COLECCIÓN DE DATOS DE ESTA MANERA:
datos = {'Col1': [1, 2, 3, 4],
        'Col2': [1, 3, 5, 7],
        'Col3': [1, 2, 4, 6]}


class ExemploTaboa(QTableWidget):
    #TENEMOS QUE PONER ESTOS PARÁMETROS EN EL INIT PARA QUE FUNCIONE
    def __init__(self, datos, *args):
        #DECLARAMOS EL QTABLE
        QTableWidget.__init__(self, *args)
        #METEMOS LA COLECCIÓN EN UNA VARIABLE
        self.datos = datos
        #ACCEDEMOS AL MÉTODO
        self.asignarDatos()
        #para que funcione ??
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