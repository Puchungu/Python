from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QPushButton,QLineEdit,QLabel)
import sys

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        boton = QPushButton("Haz click Aquí")
        boton.clicked.connect(self.boton_clickeado)
        edit = QLineEdit()
        edit.textChanged.connect(self.texto_cambiado)
        self.setCentralWidget(edit)

    def boton_clickeado(self):
        print("Botón clickeado")
    def texto_cambiado(self):
        print("haz escrito algo")

app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()