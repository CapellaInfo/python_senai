from perguntas import perguntas
import locale
import random

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def jogar():
    money = 0
    decisao_continuar = True
    perguntas_aleatorias = [] # lista
    perguntas_nivel = {} # dicionario


    for pergunta in perguntas:
        dificuldade = pergunta["dificuldade"]
        if dificuldade not in perguntas_nivel:
            perguntas_nivel[dificuldade] = []
        perguntas_nivel[dificuldade].append(pergunta)

    for dificuldade in ["fácil", "média", "difícil"]:
        if dificuldade in perguntas_nivel:
            perguntas_nivel = perguntas_nivel[dificuldade]
            random.shuffle(perguntas_nivel)
            perguntas_aleatorias.extend(perguntas_nivel)


    while decisao_continuar:
        for pergunta in perguntas_aleatorias:
            print(pergunta["pergunta"])
            for alternativa in pergunta["alternativas"]:
                print(alternativa)
            resposta = input("Escolha uma alternativa: ")
            if resposta.upper() == pergunta["resposta"]:
                print("Resposta CORRETA!\n")
                money += 100000
                print
            else:
                print("Resposta ERRADA.")
            if pergunta == perguntas_aleatorias[-1]:
                decisao_continuar = False
                break
            decisao = input("Deseja PARAR, digite sair?")
            if decisao.lower() == 'sair':
                decisao_continuar = False
                print("Parabéns!!! Você decidiu parar e ganhou: " + locale.currency(money, grouping=True))
                break

    print("Fim do jogo!")
    print("Você Ganhou: " + locale.currency(money, grouping=True))

jogar()