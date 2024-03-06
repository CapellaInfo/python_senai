from turtle import color
import matplotlib.pyplot as plt
import numpy as np

# Dados fictícios de preços médios diários para duas ações (em dólares)
preco_medio_acao1 = np.array([50, 52, 48, 55, 53, 51, 49, 50, 54, 52]) # 1x10
preco_medio_acao2 = np.array([120, 122, 118, 125, 123, 121, 119, 120, 124, 122])

# Número de ações que o investidor possui de cada empresa
acoes_acao1 = 100 # Exemplo: o investidor possui 100 ações da Ação 1 #  1x1 
acoes_acao2 = 50  # Exemplo: o investidor possui 50 ações da Ação 2

dias_acao = [1,2,3,4,5,6,7,8,9,10]

# Calculando o valor do investimento em cada dia
valor_dia_acoes1 = np.dot(acoes_acao1, preco_medio_acao1)
print(valor_dia_acoes1)

valor_dia_acoes2 = np.dot(acoes_acao2, preco_medio_acao2)
print(valor_dia_acoes2)
# Calculando o patrimônio total do investidor em cada dia
# patrimonio_dia = preco_medio_acao1[0] + preco_medio_acao2[0]
patrimonio_dia = valor_dia_acoes1 + valor_dia_acoes2
print(patrimonio_dia)

# Exibindo os resultados diariamente
for dias in patrimonio_dia:
    print(f'Dia: {dias}')

# Plot o gráfico da evolução patrimonial do investidor
plt.plot(dias_acao, patrimonio_dia)
plt.xlabel('Dias')
plt.ylabel('Patrimonio')
plt.title('Análise Patrimônio por dia')
plt.show()

plt.plot(dias_acao, patrimonio_dia, label='patrimonio total', marker='o', linestyle='-', color='b')
plt.plot(dias_acao, valor_dia_acoes1, label='acoes 1', marker='o', linestyle='-', color='g')
plt.plot(dias_acao, valor_dia_acoes2, label='acoes 2', marker='o', linestyle='-', color='r')

plt.xlabel('Dia')
plt.ylabel('Valor ($)')
plt.title('Evolução Patrimonial e de Ações de Investidor')
plt.grid(True)
plt.legend()
plt.show()
