# Crie três variáveis, a, b e c, representando os coeficientes de uma equação quadrática (ax^2 + bx + c).
# Calcule as raízes da equação usando a fórmula de Bhaskara.
a = 1
b = -10
c = 25

delta = (b**2) - 4 * a * c

if a == 0:
    print("O valor de a, deve ser diferente de 0")
elif delta < 0:
    print("Sem raízes reais")
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

print(x1)
print(x2)

# Implemente um programa que converta um valor em dólares para outras moedas 
# (por exemplo, euros e libras). Solicite ao usuário o valor em dólares e a taxa de conversão.

option = int(input("Informe a conversão desejada! 1 - Euro | 2 - Reais"))


taxa_euro = 0.93
taxa_real = 4.97

if option == 1:
    value = float(input("Informe o valor em dólares: "))
    euro = taxa_euro * value
    print(f"O valor correspondente é {euro} euros!")
elif option != 1 or option != 2:
    print("ERRO!")
else:
    value = float(input("Informe o valor em dólares: "))
    real = taxa_real * value
    print(f"O valor correspondente é {real} reais!")
    

