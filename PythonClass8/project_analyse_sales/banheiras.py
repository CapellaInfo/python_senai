import pandas as pd
import yaml
import matplotlib.pyplot as plt

# Carregar os dados dos funcionários a partir do arquivo YAML
with open('PythonClass8/project_analyse_sales/empresa.yaml', 'r') as file:
    dados = yaml.safe_load(file)


# Tabela de Vendas
df_vendas = pd.DataFrame(dados['vendas'])

print(df_vendas.describe())
print(df_vendas.head())

# Tabela de Clientes
df_cliente = pd.DataFrame(dados['comportamento_do_cliente'])
print(df_cliente.describe())
print(df_cliente.head())

print(df_cliente.copy())


# Tabela de Produtos
df_produto = pd.DataFrame(dados['desempenho_do_produto'])
print(df_produto.describe())
print(df_cliente.head())
