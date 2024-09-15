"""
Problema: En un pequeño negocio de comidas rápidas, 
el cajero debe tomar el pedido del cliente y determinar cuántos platillos necesita y que platillos del menu,
El sistema actual es manual y esto causa retrasos en la atención, Por lo tanto, 
se necesita una pequeña aplicación que permita al cajero seleccionar rápidamente 
el tipo de bplatillo (usando un ComboBox), la cantidad de cada uno (usando un SpinBox), 
"""

"""
Como podemos observar este codigo presenta un ComboBox y un Spinbox, el primero mostrando los diferentes platillos en el menu
y el segundo mostrando la cantidad de cada platillo que se puede pedir, facilitando al cajero la seleccion mejorando la rapidez de la atencion 
despues muestra el desgloce de la cantidad y que platillo selecciona el cliente, esto da una claridad en la informacion al cliente y una satisfaccion
al ser atendido de manera rapida
"""

from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout,QComboBox,QSpinBox,QPushButton)
import sys

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio propio")

        #widget central
        central = QWidget()

        #Creamos los layouts
        layout = QVBoxLayout()

        #creamos los widgets 
        self.lbl1= QLabel("Bienvenidos al sistema de carniceria las cuadras")
        self.lbl2 = QLabel("Selecciona el menu del cliente")
        self.lbl3 = QLabel("Selecciona la cantidad a comprar")
        self.CB = QComboBox()
        self.SB = QSpinBox()
        self.button = QPushButton("Mostrar orden")
        self.lbl4 = QLabel("")

        #agregarle opciones al combobox
        self.CB.addItem("Pollo a la plancha")
        self.CB.addItem("Carne a la plancha")
        self.CB.addItem("Hamburguesa")

        #set rango del SB y no input text
        self.SB.setRange(1,10)
        self.SB.lineEdit().setReadOnly(True)

        #signal del boton
        self.button.clicked.connect(self.showorder)

        #agregar widgets al layout
        layout.addWidget(self.lbl1)
        layout.addWidget(self.lbl2)
        layout.addWidget(self.CB)
        layout.addWidget(self.lbl3)
        layout.addWidget(self.SB)
        layout.addWidget(self.button)
        layout.addWidget(self.lbl4)


        central.setLayout(layout)
        self.setCentralWidget(central)

    def showorder (self):
        food = self.CB.currentText()
        quantity = self.SB.value()
        self.lbl4.setText(f"Tu orden es: {food} x {quantity}")
        

app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()