import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("malenia.csv") #se lee el csv y se asigna a df
print(df)
frecuencia = df["Level"].value_counts().sort_index() #sort_index para ordenar los niveles en orden ascendete y con value_counts se saca la freuencia de la columna Level
plt.plot(frecuencia.index, frecuencia.values) #se asigna el eje x a indices y "Y" a la frecuencia y se crea el grafico 
plt.title('Niveles del host') #titulo de la grafica
plt.xlabel('Nivel') #label eje x
plt.ylabel('Frecuencia') #label eje y
plt.show() #mostrar la grafica

"""
La gráfica muestra la frecuencia del nivel del host en el juego que ha muerto contra Malenia (un jefe del juego).
 Los niveles varian bastantes poodemos observar que el nivel con menos freuencia se encuentra entre el rango de 160 y 170
 y el nivel que con mas freuencia se encuentra en 180.
"""

#Link del dataset
"""
https://www.kaggle.com/datasets/jordancarlen/host-deaths-to-malenia-blade-of-miquella
"""