# Leia 20 números inteiros e armazene-os em um vetor
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
par = []
impar = []
# Armazene os pares no vetor PAR
for itens in numbers:
    if itens % 2 == 0:
        par.append(itens)
    else:
        impar.append(itens)
# Armazene os ímapres no vetor IMPAR
# Imprima os três vetores
print(f'Pares: {par}')
print(f'Ímpares: {impar}')