from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout
from PIL import Image
from PyQt5.QtGui import QPixmap
import sys 
import io 

#conversion de imagen a bits
def convertir(imagen):
    arreglo = io.BytesIO()
    imagen.save(arreglo, format='jpeg')
    imagenv = QPixmap()
    imagenv.loadFromData(arreglo.getvalue())
    return imagenv

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Imagen en ventana")

#convirtiendo la imagen
img = Image.open("/users/nelso/downloads/a.jpg").resize((300,200))
mapa = convertir(img)

label = QLabel()
label.setPixmap(mapa)
layout = QVBoxLayout()
layout.addWidget(label)
ventana.setLayout(layout)
ventana.show()
sys.exit(app.exec())



