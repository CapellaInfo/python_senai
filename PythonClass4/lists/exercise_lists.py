# Manipulação de Listas:
# Crie uma lista de números inteiros e ordene-a em ordem crescente.
list_1 = [1,2,3,4,5,6,7,8,9]
print(list_1)
# Adicione o número 10 ao final da lista.
list_1.append(10)
print(list_1)
# Remova o elemento de valor 5 da lista.
list_1.remove(5)
print(list_1)


# Slicing e Operações:
# Crie uma lista com os primeiros 10 números inteiros.
list_2 = [1,2,3,4,5,6,7,8,9]
# Utilize o slicing para criar uma sublista com os números pares.
sublist = list_2[1::2] # começa no índice 1 e vai dois a dois
print(sublist)
# Inverta a ordem da sublista criada.
list_2.reverse()
print(list_2)


# Listas Aninhadas:
# Crie uma lista aninhada contendo duas sublistas: 
# uma com nomes de cores e outra com códigos hexadecimais correspondentes.
list_aninhada = [["red", "green", "blue"], ["000", "111", "010"]]
# Acesse e imprima o código hexadecimal da cor "verde".
print(list_aninhada[0][1])





