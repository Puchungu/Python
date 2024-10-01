from PIL import Image
imagen_or = Image.open("/users/nelso/downloads/a.jpg")
imagen_du = imagen_or.save("/users/nelso/downloads/a.jpg")
imagen2 = Image.open("/users/nelso/downloads/a.jpg")
imagen2.show()