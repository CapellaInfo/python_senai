# Crie uma função que receba uma string como entrada e retorne True se ela for um palíndromo 
# (lê-se igual de trás para frente), e False caso contrário.
def palindromo(texto):
    texto = texto.lower().replace(" ", "")  # Remover espaços e converter para minúsculas
    return texto == texto[::-1]

frase_usuario = input("Digite uma frase para verificar se é um palíndromo: ")
resultado_palindromo = palindromo(frase_usuario)
print(f"A frase é um palíndromo: {resultado_palindromo}")

# Implemente um programa que recebe uma frase do usuário e identifica a palavra mais longa na frase.
frase_usuario = input("Digite uma frase: ")
palavras = frase_usuario.split()
palavra_mais_longa = max(palavras, key=len)
print(f"A palavra mais longa na frase é: {palavra_mais_longa}")