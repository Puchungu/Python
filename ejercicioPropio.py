'''
Una problematica en mi entorno es a la hora de organizar nuestro tiempo ya que muchas veces se nos olvidan las cosas
o simplemente no sabemos que cosas tenemos que hacer ya sea en el dia, en el mes, etc
'''

#Que hace nuestra aplicacion?
'''
Nuestra aplicacion va a realizar una lista de tareas para nuestro usuario ya que muchas veces las apps de tareas convencionales estan muy cargadas de capacidades 
que ni el mismo usuario comprende, es por eso que vamos a realizar esta app que le va a permitir al usuario eliminar, agregar y mostrar todas las tareas que el ingrese
'''

class Tarea: #creamos una clase llamada Tarea
    def __init__(self, descripcion): #creamos el constructor
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self): #funcion marcar_completa
        self.completada = True

    def __str__(self): #__str___ lo usamos para representar un objeto como cadena de texto y cuando llamamos un print
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"

class ListaDeTareas: #clase listaDeTareas
    def __init__(self): #constructor
        self.tareas = []

    def agregar_tarea(self, descripcion): #fucnion para agregar tarea
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)

    def eliminar_tarea(self, descripcion): #funcion para eliminar tarea comparando la descripcion
        self.tareas = [tarea for tarea in self.tareas if tarea.descripcion != descripcion]

    def mostrar_tareas(self): #funcion para mostrar la tarea 
        if not self.tareas:
            print("No hay tareas.")
        for tarea in self.tareas:
            print(tarea)
    def marcar_tarea_completada(self,descripcion): #funcion para marcar una tarea como completada comparando la descripcion
        for tarea in self.tareas:
            if tarea.descripcion == descripcion:
                tarea.marcar_completada()
                break

def main(): #funcion de menu principal
    lista_de_tareas = ListaDeTareas()
    
    while True:
        print("\nOpciones:")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar tareas")
        print("4. Marcar tarea como completada")
        print("5. Salir")
        
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == '1':
            descripcion = input("Ingrese la descripción de la tarea: ")
            lista_de_tareas.agregar_tarea(descripcion)
        elif opcion == '2':
            descripcion = input("Ingrese la descripción de la tarea a eliminar: ")
            lista_de_tareas.eliminar_tarea(descripcion)
        elif opcion == '3':
            lista_de_tareas.mostrar_tareas()
        elif opcion == '4':
            descripcion = input("Ingrese la descripción de la tarea a marcar como completada: ")
            lista_de_tareas.marcar_tarea_completada(descripcion)
        elif opcion == '5':
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

main()
