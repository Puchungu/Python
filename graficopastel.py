import matplotlib.pyplot as plt

restaurantes = ['TacoBell','Pizza Hut','Wendys','McDonals','ChinaWok']
Frecuecia = [1,15,11,2,5]
colores = ['purple','blue','yellow','green','red']
plt.title("Grafico de Pastel")
plt.xlabel("Restaurantes")
plt.ylabel("Frecuencia")
plt.pie(Frecuecia,labels = restaurantes, colors = colores,autopct="%1.1f%%")
plt.show()