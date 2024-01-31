# Definindo uma função
name = input("Digite seu nome: ")
def saudacao(nome):
    return f"Olá, {nome}!"

# Chamando a função
mensagem = saudacao(name)
print(mensagem)
