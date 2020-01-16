from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication, QPushButton,QSizePolicy)
import sys


class Aplication(QWidget):
    def __init__(self):
        super().__init__()

        btn1 = QPushButton("Boton1")
        btn2 = QPushButton("Boton2")
        btn3 = QPushButton("Boton3")
        btn4 = QPushButton("Boton4")
        btn5 = QPushButton("Boton5")
        btn6 = QPushButton("Boton6")
        #PARA QUE FUNCIONE CORRECTAMENTE DE ESTA MANERA, AÑADIR MINIMUN HEIGHTS O WITHS
        #btn3.setMinimumHeight(55)
        #O ESTO:
        btn3.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1, 1, 2)
        grid.addWidget(btn3, 1, 0, 2, 1)
        grid.addWidget(btn4, 1, 1, 1, 2)
        grid.addWidget(btn5, 2, 1)
        grid.addWidget(btn6, 2, 2)

        self.setLayout(grid)
        # self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Exemplo de Grid")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    exemplo = Aplication()
    sys.exit(app.exec())
