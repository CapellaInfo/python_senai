#Duo_moura_2024
import pandas as pd
import yaml
import matplotlib.pyplot as plt

# Carregar os dados dos funcionários a partir do arquivo YAML
with open('PythonClass7/dados_funcionarios.yaml', 'r') as file:
    dados_yaml = yaml.safe_load(file)


# Converter para DataFrame
df = pd.DataFrame(dados_yaml['funcionarios'])

print("1. Análise Exploratória")
print(df.head()) # Visualizar as primeiras linhas
print("============================")
print(df.info())  # Informações sobre os tipos de dados e valores nulos
print("============================")
print(df.describe()) # Estatísticas descritivas básicas

# Seleção e Filtragem de Dados
print("Funcionários com idade maior que 30 anos")
funcionario_maior_30 = df[df['idade'] > 30]
print(funcionario_maior_30)

print("Funcionários com Salário maior que 4000")
funcionario_maior_4000 = df[df['salario'] > 4000]
print(funcionario_maior_4000)

print("Funcionário(a) com maior salário")
maior_salario = df.max()
print(maior_salario)

# Manipulação de dados
print("Salário com aumento de 10%: ")
df['salario_aumento'] = df['salario'] * 1.10
print(df)

# Agregação de dados
salario_medio = df['salario'].mean()
print(f'Salário médio antes do ajuste: {salario_medio:.2f}')

salario_medio_a = df['salario_aumento'].mean()
print(f'Salário médio depois do ajuste: {salario_medio_a:.2f}')

print("Idade média dos funcionários:")
idade_media = df['idade'].mean()
print(idade_media)

print("Salário dos funcionários:")
salario_medio_all = df['salario'].sum()
print(salario_medio_all)