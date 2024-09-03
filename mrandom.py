#Modulo Random 
"""
Depende de la funcion random
Genera numeros pseudo aleatorio (no se pueden generar completamente aleatorios de manera matematica).
random() - retorna el siguiente numero flotante en el rango 0.0 hasta 1.0
radrange()
choice()
shuffle()
simple ()
"""

#import random
from random import random,randrange,randint,choice,shuffle,sample
print(random())
print(randrange(0,10,2))#0,2,4,6,8
print(randint(0,10))

lista = ["cocacola","agua","te helado","cafe"]

print(choice(lista))

lista2 = [25,6,7,8,3,1]
shuffle(lista2)
print(lista2)

lista3 = ["zanahorias", "lechuga", "pepino", "repollo"]
print(sample(lista3,2))
