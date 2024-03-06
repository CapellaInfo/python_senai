import numpy as np

my_array = np.array([[1, 2, 3], 
                     [4, 5, 6], 
                     [7, 8, 9]])
print(my_array[1, 2])

# Para calcular a soma dos elementos diagonais de uma matriz NumPy, usamos numpy.trace()
diagonal_sum = np.trace(my_array)
print(f"Soma diagonal: {diagonal_sum}")

# Número de Linhas e Colunas de uma Matriz: Para encontrar o número de linhas e colunas de uma matriz, 
# usamos a função numpy.shape. Ela retorna uma tupla de inteiros representando o tamanho 
# de cada dimensão da matriz. Aqui está um exemplo:
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
num_linhas, num_colunas = np.shape(matriz)
print(f"Número de linhas: {num_linhas}")
print(f"Número de colunas: {num_colunas}")

# Verificar se um Array NumPy Contém uma Linha Específica: 
# Para verificar se um array NumPy contém uma linha específica, podemos usar a função numpy.isin(). 
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
linha_especifica = np.array([4, 5, 6])
contem_linha = np.isin(matriz, linha_especifica).all(axis=1).any()
print(f"Contém a linha específica? {contem_linha}")

# Trocar Dois Eixos de uma Matriz: Para trocar dois eixos de uma matriz, podemos usar 
# numpy.transpose() ou simplesmente .T
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz_transposta = np.transpose(matriz)
# Ou, alternativamente: matriz_transposta = matriz.T
print("Matriz original:")
print(matriz)
print("Matriz transposta:")
print(matriz_transposta)



