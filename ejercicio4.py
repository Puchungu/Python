from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout,QPushButton,QLineEdit,QHBoxLayout)
import sys

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio 3")

        #widget central
        central = QWidget()

        #Creamos los layouts
        vlayout = QVBoxLayout()
        hlayout1 = QHBoxLayout()

        #creamos los widgets 
        self.editName = QLineEdit("Introduce tu nombre completo")
        self.editRaza = QLineEdit("Introduce tu ID")
        self.editEdad = QLineEdit("Introduce tu edad")
        self.labelname = QLabel()
        self.labelID = QLabel()
        boton = QPushButton("Haz click aqui")


        #Conectando el boton con los edit 
        boton.clicked.connect(self.AsignarALbL)

        #agregar widgets al layout
        hlayout1.addWidget(self.editName)
        hlayout1.addWidget(self.editRaza)
        hlayout1.addWidget(self.editEdad)
        hlayout1.addWidget(boton)
        vlayout.addWidget(self.labelname)
        vlayout.addWidget(self.labelID)


        #agregar los h layout al vlayout
        vlayout.addLayout(hlayout1)

        central.setLayout(vlayout)
        self.setCentralWidget(central)


    def AsignarALbL(self):
        name = self.editName.text()
        self.labelname.setText(name)
        ID = self.editID.text()
        self.labelID.setText(ID)
        

app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()