import random



def jogar():

    print("-----------------------------------------------------")
    print("JOGO DE ADIVINHAÇÃO - DESCUBRA O VALOR DO N° SECRETO!")
    print("-----------------------------------------------------\n")

    validacao_nivel = 0
    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    while (validacao_nivel == 0):
        nivel = int(input("Escolha o nível de dificuldade.\n(1)Fácil (2) Médio (3) Difícil: "))
        if (nivel != 1 and nivel != 2 and nivel != 3):
            print("Nível informado inválido!\n")
        else:
            validacao_nivel = 1

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):

        print("\nTentativa #{} de #{}".format(rodada, total_tentativas))
        chute = int(input("Digite um valor entre 1 e 100: "))

        if (chute < 1 or chute > 100):
            print("Número inválido! Você perdeu uma tentativa.")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto

        if (acertou):
            print("Certo! Você ganhou.\n")
            break
        else:
            if (maior):
                print("Errado! Seu chute foi maior que o n° secreto!")
            else:
                print("Errado! Seu chute foi menor que o n° secreto!")
            if(rodada == total_tentativas):
                print("\nO número secreto era {}.".format(numero_secreto))

        pontos -= abs(numero_secreto - chute) #modulo da diferença entre o n° secreto e o chute

    print("Fim do jogo! Você fez {} pontos.".format(pontos))

if(__name__ == "__main__"):
    jogar()



