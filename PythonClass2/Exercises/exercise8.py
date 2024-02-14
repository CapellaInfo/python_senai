# Implemente um jogo de adivinhação em que o programa escolhe um número aleatório e o jogador deve 
# adivinhar. Forneça dicas se o palpite do jogador estiver próximo do número correto.
import random

numero_aleatorio = random.randint(1, 100)
tentativas = 0

while True:
    palpite = int(input("Faça um palpite: "))
    tentativas += 1

    if abs(palpite - numero_aleatorio) <= 10:
        print("Está quente!")
    else:
        print("Está frio.")

    if palpite == numero_aleatorio:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break

# Desenvolva uma calculadora que permita ao usuário realizar operações básicas 
# (soma, subtração, multiplicação, divisão) e operações avançadas (potenciação, raiz quadrada). 
# Utilize funções para cada operação.
def calculadora():
    operacao = input("Escolha a operação (+, -, *, /, **, sqrt): ")

    if operacao == "sqrt":
        num = float(input("Digite um número para a raiz quadrada: "))
        resultado = num**0.5
    else:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            resultado = num1 / num2
        elif operacao == "**":
            resultado = num1 ** num2
        else:
            print("Operação inválida.")
            return

    print(f"Resultado: {resultado}")

calculadora()
