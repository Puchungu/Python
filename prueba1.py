from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PIL import Image
import sys
import io

# Conversión de imagen a QPixmap usando PIL
def convertir_a_pixmap(imagen):
    arreglo = io.BytesIO()
    imagen.save(arreglo, format='JPEG')  # Guardamos la imagen en bytes en formato JPEG
    imagen_en_bytes = arreglo.getvalue()  # Obtenemos los bytes de la imagen
    pixmap = QPixmap()
    pixmap.loadFromData(imagen_en_bytes)  # Cargamos el QPixmap con los datos en bytes
    return pixmap

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Imagen en ventana")

# Cargando la imagen con PIL
ruta_imagen = "/users/nelso/downloads/a.jpg"
try:
    img = Image.open(ruta_imagen)  # Abriendo la imagen con PIL
    mapa = convertir_a_pixmap(img)  # Convertimos la imagen a QPixmap

    # Configurando QLabel para mostrar la imagen
    label = QLabel()
    label.setPixmap(mapa)
    label.setScaledContents(True)  # Escalar la imagen para ajustarse al QLabel si es necesario

    # Configurando el layout
    layout = QVBoxLayout()
    layout.addWidget(label)
    ventana.setLayout(layout)

    ventana.show()
except FileNotFoundError:
    print(f"No se pudo encontrar la imagen en la ruta: {ruta_imagen}")
except Exception as e:
    print(f"Error al cargar la imagen: {e}")

sys.exit(app.exec_())