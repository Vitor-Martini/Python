import adivinhacao
import forca

validacao_jogo = 0

while (validacao_jogo == 0):
    jogo = int(input("Escolha um jogo!\n(1) Adivinhação (2) Forca: "))
    if (jogo != 1 and jogo != 2):
        print("Opção inválida!\n")
    else:
        validacao_jogo = 1

if (jogo == 1):
    adivinhacao.jogar()
elif (jogo == 2):
    forca.jogar()


