import Calculadoras as Calc
print("---Bienvenidos a la calculadora de volumenes---")
Opcion = int(input("Eliga una de las siguientes opciones \n 1.Calcular Volumen de Cilindro \n 2.Calcular Volumen de Cono \n 3.Calcular Volumen de Esfera\n"))
if (Opcion == 1):
    radio = int(input("Ingresa el radio: "))
    altura = int(input("Ingresa la altura: "))
    Calc.volumen_cilindro(radio,altura)   
elif(Opcion==2):
    radio = int(input("Ingresa el radio: "))
    altura = int(input("Ingresa la altura: "))
    Calc.volumen_cono(radio,altura)
elif (Opcion==3):
    radio = int(input("Ingresa el radio: "))
    Calc.volumen_esfera(radio)




   