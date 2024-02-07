# Listas (mutáveis)
frutas = ["maçã", "banana", "uva"]
numeros = [1, 2, 3, 4, 5]

# Adicionando elementos a uma lista
frutas.append("laranja")
frutas.append("morango")
print(frutas)

# Acessando elementos
print(frutas[0])
print(frutas[:4])



# Tuplas (imutáveis)
coordenadas = (4, 5, 6, 7)
cores_rgb = (255, 0, 0)
print(coordenadas[0], coordenadas[3])

for fruta in frutas:
    print(fruta)

for coord in coordenadas:
    print(coord)


