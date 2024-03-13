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