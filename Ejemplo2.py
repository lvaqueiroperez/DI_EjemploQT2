from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication)
import sys

#EJEMPLO DE VENTANA SIMPLE SIN EL USO DE QTDESIGNER
class Aplication(QWidget):
    def __init__(self):
        #USANDO PyQT5,COMO HEREDAMOS DE QWIDGET, HAY QUE PONER "SUPER"
        super().__init__()
        #CREACIÓN DE COMPONENTES:
        lblTitulo = QLabel("Titulo")
        lblAutor = QLabel("Autor")
        lblResumo = QLabel("Resumo")

        editTitulo = QLineEdit()
        editAutor = QLineEdit()
        txtResumo = QTextEdit()
        #CREAMOS UNA GRID DONDE PONDREMOS TODOS LOS ELEMENTOS:
        grid = QGridLayout()
        #ESPACIO ENTRE CADA ELEMENTO CON "setSpacing()"
        grid.setSpacing(10)
        #AÑADIMOS LOS ELEMENTOS CON LA POSICIÓN FILA/COLUMNA Y SI QUEREMOS CON LAS POSICIONES FINALES, TAMBIÉN FILA/COLUMNA, PARA SABER CUÁNTO OCUPARÁN
        grid.addWidget(lblTitulo, 1, 0)
        grid.addWidget(editTitulo, 1, 1)
        grid.addWidget(lblAutor, 2, 0)
        grid.addWidget(editAutor, 2, 1)
        grid.addWidget(lblResumo, 3, 0)
        grid.addWidget(txtResumo, 3, 1, 5,1)  # Los 2 primero son la posicion en la cuadricula y los 2 las últimas coordenadas
        #AÑADIMOS LA GRID A LA VENTANA PRINCIPAL
        self.setLayout(grid)
        #TAMAÑO PREDETERMINADO DE LA VENTANA PRINCIPAL
        self.setGeometry(300, 300, 350, 300)
        #TÍTULO DE LA VENTANA PRINCIPAL
        self.setWindowTitle("Exemplo de Grid")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    exemplo = Aplication()
    sys.exit(app.exec())
