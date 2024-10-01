from PIL import Image

#forma1
imagent = Image.open("/users/nelso/downloads/a.jpg").rotate(45)

imagent2 = Image.open("/users/nelso/downloads/a.jpg").resize((300,200))
#forma2
#imagenrotada = imagent.rotate(45, expand=True)
imagent2.show()