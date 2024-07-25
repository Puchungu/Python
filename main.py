#run without debugging
print("Programacion 3")
print("------------------------- DECLARANDO VARIABLES----------------------------")
#declarando una variable
variable1 = "valor"
variable2 = 20
variable3 = 12.2
variable4 = True
variable5 = [12,4,79,23,41]
print("-------------------------- OPERADORES ARITMETICOS---------------------------")
#Operadores aritmeticos + - * / // ** %

num1 = 20
num2 = 3

divisionEntera = print(num1//num2)
reiduoDivision = print(num1%num2)

print("------------------------ AND -----------------------------")
#Operadores logicos and, or, not

print(True and True)
print(True and False)
print(False and False)
print(False and True)

print("--------------------------- OR --------------------------")
print(True or True)
print(True or False)
print(False or False)
print(False or True)

#Operadores de comparacion <> <= => == =!
print("-------------------------- OPERADORES COMPARACION---------------------------")
print(9<10)
print(10>10)
print("Python" == "Python")

print("---------------------------- CALCULAR EL AREA DE UN TRIANGULO-------------------------")
base = input("Ingrese la base: ")
altura = input("Ingrese la altura: ")
area = print("El area del triangulo es: ", (float(base)*float(altura))/2)

print("---------------------------- CONVERTIR C a F-------------------------")

C = float(input("Ingrese los grados en celsius: "))
Farenheit = print("Los grados " , C , "convertido a farenheit son: ", ((C * 9/5) + 32))


