nombre = "Nelson"
apellido = "Alvarenga"
nombre2 = "nelson alvarenga"

#F-String 
print("Hola, mi nombre es", nombre + " y mi apellido es", apellido)

#title()
print("mi nombre usando title se veria asi: ",nombre2.title())

#replicacion
variable = "Hola"
print(variable*10)

#funcion (def)
def Saludar():
    print("Hola Mundo")
Saludar()

#Parametros y Argumentos




#funcion (def)
def Saludar():
    print("Hola Mundo")
Saludar()


def doblar_valor(numero): #numero seria parametro
    n2 = numero*2
    return n2
print(doblar_valor(6)) #6 es el argumento

#2 parametros hay que pasarle 2 argumentos 
def describir(tipom, nombrem):
    print(f"Mi mascota es un {tipom} y se llama {nombrem}")
describir("Loro", "Pancho")

#Argumentos "keyword"
def describir(tipom, nombrem):
    print(f"Mi mascota es un {tipom} y se llama {nombrem}")
describir(nombrem = "Pancho", tipom = "loro")

#parametros default se tienen que declarar por ultimo
def describir(tipom, nombrem="Pancho"):
    print(f"Mi mascota es un {tipom} y se llama {nombrem}")
describir("Perro")

#Parametros *args y **args, reciben n cantidad de parametros es decir cualquier cantidad que sea necesaria 
def inf(nombre,carnet, carrera,*materias):
    print(f"Informe del estudiante {nombre} con carnet {carnet} y de la carrera {carrera}, lleva las materias de: ")
    for materia in materias:
        print(f"*{materia}")
inf("Nelson", "SMSS127921","ING SISTEMAS","Ingles Basico","Circuitos Digitales","Programacion","Base de datos","Estadistica")

#valor de retorno, es un tipo de valor que la funcion puede llegar a generar
def doblar_valor(numero): 
    n2 = numero*2
    return n2
print(doblar_valor(6)) 

def mult():
    total = 3*5
    return total

print("Ingresa un valor que quieras multiplicar por 15")
valor = float(input())
print(valor*mult())


