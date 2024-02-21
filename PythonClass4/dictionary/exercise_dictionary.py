# Manipulação de Dicionários:
# Crie um dicionário representando informações sobre um livro (título, autor, ano de publicação).
books = {"título": "1984", 
         "autor":"George ", 
         "ano":"2023"}
print(books)
# Adicione uma nova chave-valor ao dicionário representando a quantidade de páginas do livro.
books["páginas"] = "200"
print(books)


# Iteração e Impressão:
# Crie um dicionário com nomes de países e suas respectivas capitais.
paises_capitais = {
    'Brasil': 'Brasília',
    'Estados Unidos': 'Washington, D.C.',
    'França': 'Paris',
    'Alemanha': 'Berlim',
    'Japão': 'Tóquio',
    'China': 'Pequim',
    'Rússia': 'Moscou',
    'Índia': 'Nova Delhi',
    'Canadá': 'Ottawa',
    'Austrália': 'Camberra'
}
print(paises_capitais)
# Utilize um loop para imprimir cada país e sua capital.
for countries in paises_capitais:
    capitais = paises_capitais[countries]
    print(f"A capital de {countries} é {capitais}.")


# Remoção de Itens:
# Crie um dicionário com pares chave-valor representando um inventário de produtos.
products = {
    '01': 'Cadeira',
    '02': 'Colher',
    '03': 'Macarrão',
    '04': 'Arroz',
    '05': 'Feijão'
}
print(products)
# Remova um item do inventário utilizando sua chave.
del products['01']
print(products)