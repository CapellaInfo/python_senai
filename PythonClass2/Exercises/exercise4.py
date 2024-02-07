# Crie duas variáveis booleanas, tem_sol e tem_chuva, representando condições climáticas. 
# Utilize essas variáveis em uma estrutura condicional para decidir se é um dia agradável ou não.
tem_sol = True
tem_chuva = False
if tem_sol:
    print("Sunny day!!")
else:
    print("Rainy day!!")

# Solicite ao usuário dois números e use operadores lógicos para verificar se ambos são números pares. 
# Imprima o resultado.
num1 = int(input("Inform the 1º number: "))
num2 = int(input("Inform the 2º number: "))
if num1%2 == 0 and num2%2 == 0:
    print("Ambos são pares")
elif num1%2 == 0 or num1%2 == 0:
    print("Número 1 é par!")
elif num2%2 == 0 or num1%2 == 0:
    print("Número 2 é par!")
else:
    print("Não há números pares!")

# Crie uma lista de números e use uma estrutura de repetição para percorrer a lista. 
# Utilize operadores lógicos para verificar e imprimir quais números são múltiplos de 3 e ímpares.
number_list = [1, 5, 7, 10, 29, 33, 45, 60, 99]
for number in number_list:
    if number %3 == 0 and number%2 ==1:
        print(number)

# Peça ao usuário para digitar a sua idade e verifique se ela está dentro do intervalo de 18 a 65 anos. 
# Imprima uma mensagem correspondente.
age = int(input("Put your age:"))

if age >=18 and age <=65:
    print("Your age is OK!")
else:
    print("NOT OK!")

interval = range(18, 65)

if age in interval:
    print(f'{age} OK!')
else:
    print(f'{age} NO!')
