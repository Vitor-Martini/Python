import random


def jogar():

    imprimir_apresentacao()

    palavra_secreta = sortear_palavra_secreta()
    letras_acertadas = ["_" for letra in palavra_secreta]
    print(letras_acertadas, "\n")

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):

        chute = input("Qual a letra? ").upper().strip()

        if (chute in palavra_secreta):
            verificar_chute(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            desenhar_forca(erros)

        acertou = "_" not in letras_acertadas
        enforcou = erros == 7
        print(letras_acertadas, "\n")

    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu! A palavra era {}.".format(palavra_secreta))


def imprimir_apresentacao():
    print("-----------------------------------------------------")
    print("--------------------JOGO DA FORCA--------------------")
    print("-----------------------------------------------------")
    desenhar_forca(0)

def sortear_palavra_secreta():
    palavras = []
    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    return palavras[random.randrange(0, len(palavras))].upper()

def verificar_chute(palavra_secreta, chute, letras_acertadas):
    i = 0
    for letra in palavra_secreta:
        if (letra == chute):
            letras_acertadas[i] = letra

        i += 1

def desenhar_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar()
