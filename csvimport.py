import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({"Nombre": ["Juan","Maria","Pedro","Luis","Ana","Gerson","Fernando"], "Edad": [20,20,30,40,50,60,70]})

frecuencia = df["Edad"].value_counts()
plt.plot(frecuencia.index,frecuencia.values)
plt.show()