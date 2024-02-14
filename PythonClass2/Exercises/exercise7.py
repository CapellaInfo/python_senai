# Escreva uma função que receba uma lista de números e retorne outra lista contendo apenas os números 
# primos.
def numeros_primos(lista):
    return [num for num in lista if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]

numeros = [2, 5, 8, 11, 15, 18, 23]
primos = numeros_primos(numeros)
print(f"Números primos na lista: {primos}")

# Crie um programa que simule uma fila de atendimento em um banco. Utilize uma lista para representar 
# a fila e implemente funções para adicionar clientes, remover clientes e mostrar a posição de um 
# cliente específico na fila.
fila_atendimento = []

def adicionar_cliente(nome):
    fila_atendimento.append(nome)

def remover_cliente():
    if fila_atendimento:
        cliente_removido = fila_atendimento.pop(0)
        print(f"Cliente {cliente_removido} foi atendido.")
    else:
        print("Fila vazia. Nenhum cliente para atender.")

def mostrar_posicao_cliente(nome):
    if nome in fila_atendimento:
        posicao = fila_atendimento.index(nome) + 1
        print(f"O cliente {nome} está na posição {posicao} da fila.")
    else:
        print(f"O cliente {nome} não está na fila.")

adicionar_cliente("Alice")
adicionar_cliente("Bob")
adicionar_cliente("Charlie")
mostrar_posicao_cliente("Bob")
remover_cliente()

