pi = 3.1416

def volumen_cilindro(radio, altura):
    print("Calculo del Volumen de un Cilindro")
    Area = ((radio**2)*pi*altura)
    print(f"El area del cilindro es: {Area}")

def volumen_cono(radio, altura):
    print("Calculo del Volumen de un cono")
    Area = ((radio**2)*pi*altura*(1/3))
    print(f"El area del cono es: {Area}")

def volumen_esfera(radio):
    print("Calculo del Volumen de una esfera")
    Area = ((radio**3)*pi*(4/3))
    print(f"El area de la esfera es: {Area}")