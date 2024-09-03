import datetime
#print(datetime.datetime.now())
nombre = input("Hola, dime tu nombre: ")
fecha = datetime.datetime.now()



if(fecha.hour < 12):
    print("Buenos días", nombre)
elif(fecha.hour >= 12):
    print("Buenas tardes", nombre)
else: 
    print("Buenas noches", nombre)

print(fecha.strftime("%A"))