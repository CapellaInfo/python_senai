import numpy as np

# Para criar uma matriz NumPy vazia, podemos usar a função numpy.empty(shape)
empty_array = np.empty((3, 3))
print(empty_array)

# Para criar uma matriz preenchida com valores iguais a 1, podemos usar a função numpy.ones(shape)
ones_array = np.ones((2, 2))
print(ones_array)

# Para criar uma matriz preenchida com todos os zeros, podemos usar a função numpy.zeros(shape)

zeros_array = np.zeros((4, 4))
print(zeros_array)

# Para criar uma matriz com valores aleatórios entre 0 e 1, podemos usar a função numpy.random.rand(shape)
random_array = np.random.rand(3, 3)
print(random_array)

# Para selecionar elementos específicos de uma matriz NumPy, usamos a indexação por posição
my_array = np.array([[1, 2, 3], 
                     [4, 5, 6], 
                     [7, 8, 9]])
print(my_array[1, 2])  # Seleciona o elemento na segunda linha e terceira coluna (6)

# Para encontrar o valor máximo e mínimo em uma matriz, usamos numpy.max() e numpy.min()
max_value = np.max(my_array)
min_value = np.min(my_array)
print(f"Valor máximo: {max_value}, Valor mínimo: {min_value}")

# Para calcular a soma dos valores em uma matriz, usamos numpy.sum()
total_sum = np.sum(my_array)
print(f"Soma total: {total_sum}")

# Para remover entradas unidimensionais de uma matriz, usamos numpy.squeeze()
squeezed_array = np.squeeze(my_array)
print(squeezed_array)

# Adição de Matrizes: usamos o operador +
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 + matriz2
print("Resultado da adição de matrizes:")
print(resultado)

# Subtração de Matrizes: usamos o operador -
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 - matriz2
print("Resultado da subtração de matrizes:")
print(resultado)

# Multiplicação de Matrizes: Para multiplicar matrizes em Python, podemos usar a função 
# numpy.dot() ou o operador @
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = np.dot(matriz1, matriz2)
# Ou, alternativamente: resultado = matriz1 @ matriz2
print("Resultado da multiplicação de matrizes:")
print(resultado)


