from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QPushButton,
                             QLabel, QVBoxLayout, QLineEdit,QGridLayout,QFormLayout)
import sys

class VentanaMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal")
        self.setGeometry(100, 200, 300, 300)
        
        central = QWidget()  # Widget central
        boton = QPushButton("Haz click Aquí")  # Botón
        texto = QLabel("Esto es un label")  # Etiqueta
        entrada = QLineEdit()  # Campo de texto
        
        """
        layout = QVBoxLayout()  # Layout vertical QVBoxLayout
        layout.addWidget(boton)
        layout.addWidget(texto)
        layout.addWidget(entrada)
        """
        """
        layout = QGridLayout()  # Layout Grid QGridLayout
        layout.addWidget(boton,0,0)
        layout.addWidget(texto,1,1)
        layout.addWidget(entrada,2,2)
        """ 
        layout = QFormLayout()  # Layout Grid QFormLayout
        layout.addWidget(boton)
        layout.addWidget(texto)
        layout.addWidget(entrada)
        
        central.setLayout(layout)  # Asignamos el layout al widget central
        self.setCentralWidget(central)  # Establecemos el widget central de la ventana principal

# Configuración de la aplicación
app = QApplication(sys.argv)

ventana = VentanaMain()  # Creamos una instancia de VentanaMain
ventana.show()  # Mostramos la ventana

sys.exit(app.exec())  # Ejecutamos el ciclo de eventos de la aplicación





