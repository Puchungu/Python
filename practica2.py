from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QPushButton,QLineEdit,QLabel,QFormLayout)
import sys

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        boton = QPushButton("Haz click Aquí")
        boton.clicked.connect(self.boton_clickeado)
        self.setGeometry(100, 200, 300, 300)
        self.edit = QLineEdit()
        layout = QFormLayout()
        self.label = QLabel()
        central = QWidget()
        layout.addRow(boton,self.edit)
        layout.addRow(self.label)
        self.centralWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

    def boton_clickeado(self):
        #print("Botón clickeado")
        texto = self.edit.text()
        #print(texto)
        self.label.setText(texto)


app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()