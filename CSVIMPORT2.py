import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("male_teams.csv")
print(df)

frecuencia = df["fifa_version"].value_counts()
plt.pie(frecuencia.values,labels = frecuencia.index,autopct="%1.1f%%")
plt.show()