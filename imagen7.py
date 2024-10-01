from PIL import Image 
imagen = Image.open("/users/nelso/downloads/a.jpg")
imgbn = imagen.convert("L").show()
imgp = imagen.convert("P").show()