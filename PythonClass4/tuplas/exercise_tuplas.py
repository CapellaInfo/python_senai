# Operações com Tuplas:
# Crie uma tupla com os meses do ano.
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 
          'October', 'November', 'December')
print(months)
# Acesse os meses de janeiro a junho.
print(months[0:6])
# Tente adicionar um novo mês à tupla e observe o resultado.
# ERRORRRRR - IMUTABLE!!!!


# Tuplas como Chaves de Dicionários:
# Crie um dicionário onde as chaves são tuplas representando coordenadas (latitude, longitude) 
# e os valores são nomes de cidades.
coordenadas = {(40.7128, -74.0060):("Limeira"), (78.7128, -90.0060):("Japão") }
# Acesse e imprima o nome da cidade correspondente à coordenada (40.7128, -74.0060).
print(coordenadas[(40.7128, -74.0060)])
