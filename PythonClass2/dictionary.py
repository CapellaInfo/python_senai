# Dicionário chave-valor
pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "profissao": "engenheiro"
}

# Acessando valores
print(pessoa["nome"])
print(pessoa.get("idade"))

# Adicionando novo par chave-valor
pessoa["cidade"] = "São Paulo"
print(pessoa)


# Dicionário
aluno = {
    "nome": "Maria",
    "idade": 22,
    "curso": "Ciência da Computação"
}

# Acessando valores
print(aluno["nome"])
print(aluno["curso"])

# Adicionando novo valor
aluno["nota_final"] = 85
print(aluno)
