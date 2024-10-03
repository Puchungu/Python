import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("male_players.csv") #se lee el csv y se asigna a df
frecuencia = df["overall"].value_counts().sort_index() #sort_index para ordenar los niveles en orden ascendete y con value_counts se saca la freuencia de la columna overall
plt.bar(frecuencia.index, frecuencia.values) # se asigna el eje x a indices y "Y" a la frecuencia y se crea el grafico 
plt.title('Puntaje general de atributo del jugador') #titulo de la grafica
plt.xlabel('Puntaje') #colocamos un label al eje x
plt.ylabel('Frecuencia') #colocamos un label al eje y 
plt.show() # se muestra el grafico

"""
La siguiente grafica muestra el puntaje general (es decir la media del jugador tomando en cuenta todos sus atributos)
de los jugadores desde el fifa 15 al 24, podemos observar que el puntaje que tiene mas frecuencia se encuentra 
en el rango de 60 a 70 y se analiza tambien que hay muy pocos jugadores con media de 40 a 50 y hay pocos tambien con  media alta
de 80 a 90, es decir hay mas jugadores estandar que malos y muy buenos. 
"""

#Link del dataset (male_players.csv)
"""
https://www.kaggle.com/datasets/stefanoleone992/ea-sports-fc-24-complete-player-dataset
"""