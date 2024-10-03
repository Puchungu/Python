import matplotlib.pyplot as plt

dep = ['San miguel', 'San isidro', 'Miraflores', 'San borja', 'Surco']
frec = [10, 20, 30, 40, 50]
colores = ['purple','blue','yellow','green','red']
plt.title("Gráfico de Barras")
plt.xlabel("Departamentos")
plt.ylabel("Frecuencia")
plt.bar(dep, frec, color=colores)
plt.show()