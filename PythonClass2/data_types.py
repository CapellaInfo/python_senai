# int: Números inteiros.
# float: Números de ponto flutuante.
# str: Cadeias de caracteres.
# bool: Valores booleanos (True/False).
# list: Listas (coleções mutáveis).
# tuple: Tuplas (coleções imutáveis).
# dict: Dicionários (coleções de pares chave-valor).

# Conversão de Tipos (Type Casting)
numero = 42
texto = str(numero)  # Converte o número para string

texto = "42"
numero = int(texto)  # Converte a string para inteiro

# Números inteiros
idade = 25
quantidade_produtos = 100

# Números de ponto flutuante
preco_unitario = 29.99
pi = 3.14159

# Strings simples
nome = "Alice"
mensagem = 'Olá, seja bem-vindo!'

# Concatenação de strings
nome_completo = nome + " Wonderland"

# Formatação de strings
mensagem_formatada = f"Olá, {nome}! Você tem {idade} anos."
print(mensagem_formatada)

# Variáveis booleanas
tem_cafe = True
tem_cha = False

# Expressões booleanas
tem_bebida_quente = tem_cafe or tem_cha
tem_as_dois = tem_cafe and tem_cha
