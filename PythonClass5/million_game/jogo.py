from perguntas import perguntas

def jogar():
    money = 0
    decisao_continuar = True
    continuar_sair = True

    while decisao_continuar:
        for pergunta in perguntas:
            print(pergunta["pergunta"])
            for alternativa in pergunta["alternativas"]:
                print(alternativa)
            resposta = input("Qual é a sua resposta? ")
            if resposta.upper() == pergunta["resposta"]:
                print("Resposta correta!\n")
                money += 1
                print
            else:
                print("Resposta incorreta.")
            decisao = input("Deseja continuar ou sair?")
            while continuar_sair:
                if decisao.lower() == 'sair':
                    decisao_continuar = False
                    continuar_sair = False
                    break
                elif decisao.lower() == 'continuar':
                    decisao_continuar = True
                    continuar_sair = False
                else:
                    print("Informe o que deseja")

    print("Fim do jogo!")
    print("Você Ganhou: R$" + str(money) + " de Reais!")

jogar()