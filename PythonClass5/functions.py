# def nome_da_funcao(parametros):
#     # Código da função
#     return resultado

# nome_da_funcao: Identifica o nome da função, permitindo chamá-la posteriormente.
# parâmetros: São variáveis que a função aceita como entrada (argumentos).
# código da função: É o bloco de instruções que realiza a tarefa desejada.
# return: Indica o valor que a função retorna após a execução.

# Função Simples:
def saudacao(nome):
    return f"Olá, {nome}!"

# Função com Parâmetros Padrão:
def potencia(base, expoente=2):
    return base ** expoente

# Função com Retorno Múltiplo:
def opera_numeros(a, b):
    soma = a + b
    diferenca = a - b
    return soma, diferenca

print(saudacao("Rafael"))
print(potencia(5))
print(opera_numeros(4,3))


# Chamada de Funções
# resultado = nome_da_funcao(argumentos)
def calcular_quadrado(numero):
    return numero ** 2

resultado = calcular_quadrado(5)
print(resultado)  # Saída: 25


# Recursividade é a capacidade de uma função chamar a si mesma durante a execução. 
# Em Python, funções podem ser recursivas, permitindo a resolução de problemas dividindo-os 
# em subproblemas menores e resolvendo-os recursivamente. É importante incluir uma condição 
# de parada para evitar chamadas infinitas.

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

resultado = fatorial(5)
print(resultado)  # Saída: 120

# No exemplo acima, a função fatorial é recursiva, calculando o fatorial de um número n 
# chamando a si mesma. A condição de parada (n == 0 ou n == 1) evita que a recursão 
# continue indefinidamente.

