import matplotlib.pyplot as plt

restaurantes = ['TacoBell','Pizza Hut','Wendys','McDonals','ChinaWok']
Frecuecia = [1,15,11,2,5]

colores = ['purple','blue','yellow','green','red']
plt.title("Gráfico de Barras")
plt.xlabel("Restaurantes")
plt.ylabel("Frecuencia")
plt.bar(restaurantes, Frecuecia, color = colores)
# linea plt.plot(restaurantes, Frecuecia, color = colores)
plt.show()


