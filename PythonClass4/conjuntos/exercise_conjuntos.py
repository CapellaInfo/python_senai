# Operações de Conjuntos:
# Crie dois conjuntos com números inteiros.
numbers = {1, 2, 3, 4, 5, 6, 7}
numbers_two = {1, 2, 5, 7, 9, 10}
# Realize a união, interseção e diferença entre esses conjuntos.
uniao = numbers.union(numbers_two)
intersecao = numbers.intersection(numbers_two)
difference =  numbers.difference(numbers_two)

print(uniao)
print(intersecao)
print(difference)


# Remoção de Duplicatas:
# Crie uma lista com elementos duplicados.
duplicate_list = [1, 1, 2, 3, 3, 3, "Rafael", "Maria", "Rafael"]
# Converta a lista para um conjunto para remover as duplicatas.
conjunto_only = set(duplicate_list)
print(conjunto_only)
