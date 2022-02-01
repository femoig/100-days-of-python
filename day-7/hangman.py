import random
from hangman_art import stages, logo


espacos = []

def verifica_usuario_ganhou():
    if "_" not in espacos:
        return True

def reset():
    espacos.clear()

def perde_vida(vidas):
    vidas -= 1
    return vidas

def preenche_letra(letra_palpite, palavra_sorteada):
    index = 0
    for letra_sorteada in palavra_sorteada:
        if letra_palpite == letra_sorteada:
            espacos[index] = letra_palpite
        index += 1
    print(espacos)


def tentativas(palavra_sorteada):
    vidas = 6
    while True:
        letra = input("Digite uma letra para adivinhar a palavra...: ").lower()
        if letra in palavra_sorteada:
            print(letra.upper())
            preenche_letra(letra, palavra_sorteada)
            ganhou = verifica_usuario_ganhou()
            if ganhou:
                print("Parabéns você acertou!!!")
                break

        else:
            print("Errou")
            vidas = perde_vida(vidas)
            print(stages[vidas])
            if vidas == 0:
                print("GAME OVER...")
                print(f"A palavra era...: {palavra_sorteada}")
                break


def gera_espacos(palavra_sorteada):
    for letra in range(len(palavra_sorteada)):
        espacos.append("_")
    print(espacos)


def sorteia_palavra():
    lista_palavras = ["amarelo", "azul", "roxo", "rosa", "vermelho", "verde", "laranja"]
    return random.choice(lista_palavras)


def play():
    reset()
    palavra_sorteada = sorteia_palavra()
    gera_espacos(palavra_sorteada)
    tentativas(palavra_sorteada)


if __name__ == "__main__":
    print(logo)
    while True:
        play()

        sair = input("Jogar novamente? S ou N...: ")
        if sair.lower() != "s":
            quit()
