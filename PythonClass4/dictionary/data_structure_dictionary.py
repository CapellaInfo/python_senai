# Um dicionário em Python é uma coleção de pares chave-valor. 
# Cada elemento no dicionário é acessado através de uma chave única, 
# e os valores associados a essas chaves podem ser de qualquer tipo.

#Criação de Dicionários:
# Dicionário de informações sobre uma pessoa
pessoa = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}

# Dicionário vazio
configuracoes = {}

# Acesso a Valores:
# Acesso por chave
nome = pessoa['nome']  # Resultado: 'João'
print(nome)
# Modificação de Valores:

# Modificar um valor
pessoa['idade'] = 26  # Agora o dicionário é {'nome': 'João', 'idade': 26, 'cidade': 'São Paulo'}
print(pessoa)
# Adição e Remoção de Itens:

# Adicionar novo item
pessoa['profissao'] = 'Engenheiro'  # Resultado: {'nome': 'João', 'idade': 26, 'cidade': 'São Paulo', 'profissao': 'Engenheiro'}
print(pessoa)
# Remover item por chave
del pessoa['cidade']  # Resultado: {'nome': 'João', 'idade': 26, 'profissao': 'Engenheiro'}
print(pessoa)