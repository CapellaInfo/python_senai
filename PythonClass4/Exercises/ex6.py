# Leia quatro notas de 10 alunos
aluno1 = [10, 6,5,7]
aluno2 = [2,4,5,6]
aluno3 = [1,10,8,9]
aluno4 = [10,6,2,3]

sum = 0
average = 0
elements = len(aluno1)
# Calcule e armazene a média de cada aluno em um vetor
for media in aluno1:
    sum += media
    average = sum / elements
    print(average)
# Imprima o número de alunos com média maior ou igual a 7.0