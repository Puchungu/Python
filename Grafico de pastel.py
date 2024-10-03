import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("female_coaches.csv")
print(df)
frecuencia = df["nationality_name"].value_counts()
plt.pie(frecuencia.values,labels = frecuencia.index,autopct="%1.1f%%")
plt.show()

"""
Del siguiente analisis del grafico podemos observar que hay mas directoras tecnicas de Espana que de otro pais,
pero tambien podemos analizar que la segunda nacionalidad que mas hay es Francia y la tercera Inglaterra. Por lo 
tanto definimos que la presencia de las DT ha crecido sobre todo en Europa aunque existe variedad de nacionalidades
"""


#Link del dataset (female_coaches.csv)
"""
https://www.kaggle.com/datasets/stefanoleone992/ea-sports-fc-24-complete-player-dataset
"""
