import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("malenia.csv")
print(df)
frecuencia = df["Level"].value_counts().sort_index() #sort_index para ordenar los niveles
plt.plot(frecuencia.index, frecuencia.values)
plt.title('Niveles del host')
plt.xlabel('Nivel')
plt.ylabel('Frecuencia')
plt.show()

"""
La gráfica muestra la frecuencia del nivel del host en el juego que ha muerto contra Malenia (un jefe del juego).
 Los niveles varian bastantes poodemos observar que el nivel con menos freuencia se encuentra entre el rango de 160 y 170
 y el nivel que con mas freuencia se encuentra en 180.
"""

#Link del dataset
"""
https://www.kaggle.com/datasets/jordancarlen/host-deaths-to-malenia-blade-of-miquella
"""