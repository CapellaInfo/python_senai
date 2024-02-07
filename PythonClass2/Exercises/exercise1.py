# Crie duas variáveis, a e b, atribua valores e realize as seguintes operações:
from math import pi

a = 8
b = 5

soma =  (a + b)
subtração = (a - b)
multiplicação = (a * b)
divisão = (a / b)
divisão_inteira = (a // b)
resto_divisao = (a % b)
potenciação = (a ** b)

print(soma, subtração, multiplicação, divisão, divisão_inteira, resto_divisao, potenciação)

# Declare uma variável para representar o raio de um círculo e calcule sua área usando a fórmula 
# área = π * raio^2. Considere π como 3.14.

radius = input("Digite um valor: ")
area = pi * float(radius) ** 2
print(f"{area}")


