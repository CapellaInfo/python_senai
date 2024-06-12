import pandas as pd
import numpy as np

# Semente para reprodutibilidade
# Ao definir a semente (seed) para o gerador de números aleatórios, garantimos que os resultados
# sejam os mesmos toda vez que o código for executado. Isso é útil para testes e depuração.
np.random.seed(42)

# Datas ao longo de um ano
# Cria uma série de datas de 1º de janeiro de 2023 a 31 de dezembro de 2023, uma por dia.
datas = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')

# Categorias e Subcategorias
# Define categorias de produtos e suas subcategorias correspondentes.
categorias = ['Eletrônicos', 'Roupas', 'Alimentos', 'Móveis']
subcategorias = {
    'Eletrônicos': ['Celulares', 'Computadores', 'TVs', 'Câmeras'],
    'Roupas': ['Camisetas', 'Calças', 'Casacos', 'Sapatos'],
    'Alimentos': ['Frutas', 'Verduras', 'Carnes', 'Laticínios'],
    'Móveis': ['Mesas', 'Cadeiras', 'Sofás', 'Camas']
}

# Número de registros
# Define o número de registros que serão gerados. Aqui, um registro por dia do ano.
num_records = 365  # Um registro por dia

# Geração dos dados
# Inicializa um dicionário para armazenar os dados.
data = {
    'data': np.random.choice(datas, num_records),  # Escolhe aleatoriamente datas do ano
    'categoria': np.random.choice(categorias, num_records),  # Escolhe aleatoriamente categorias
}

# Adicionar subcategorias baseadas nas categorias
# Para cada categoria escolhida, escolhe aleatoriamente uma subcategoria correspondente.
data['subcategoria'] = [np.random.choice(subcategorias[cat]) for cat in data['categoria']]

# Valores de vendas e quantidade
# Gera valores de vendas aleatórios entre 20 e 500, com duas casas decimais.
data['vendas'] = np.round(np.random.uniform(20, 500, num_records), 2)
# Gera quantidades aleatórias entre 1 e 20.
data['quantidade'] = np.random.randint(1, 20, num_records)

# Criar DataFrame
# Converte o dicionário em um DataFrame do pandas.
df_vendas = pd.DataFrame(data)

# Ordenar por data
# Ordena os registros do DataFrame pela coluna de data.
df_vendas.sort_values('data', inplace=True)

# Salvar em CSV
# Salva o DataFrame em um arquivo CSV chamado 'vendas.csv', sem incluir o índice.
df_vendas.to_csv('vendas.csv', index=False)

# Mostrar os primeiros registros
# Exibe os primeiros registros do DataFrame para verificação.
print(df_vendas.head())
