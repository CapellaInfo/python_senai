import matplotlib.pyplot as plt

# Criando um gráfico simples
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 8]
z = [8, 7, 9, 6, 10]

# plt.plot(x, y)
# plt.scatter(x,y)
# plt.stem(x,y)
plt.scatter(x,y,z)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Exemplo de Gráfico')
plt.show()
