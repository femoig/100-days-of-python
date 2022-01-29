import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lista_imagens = [rock, paper, scissors]

def valida_escolha_jogador(escolha_jogador):
    if escolha_jogador > 2:
        print("Escolha inválida...Valores válidos são [0 para Pedra, 1 para Papel or 2 para Tesoura]")
        jogar_novamente()

def jogar_novamente():
    jogar_novamente = input("\nDeseja jogar novamente? S para Sim, N para Não...: ")
    if jogar_novamente.upper() == "S":
        main()
    else:
        quit()


def verifica_vencedor(escolha_jogador, escolha_computador):
    if escolha_jogador == escolha_computador:
        print("Empate!!!")
    elif escolha_jogador == 0 and escolha_computador == 2:
        print("Você ganhou!!!")
    elif escolha_jogador == 2 and escolha_computador == 1:
        print("Você ganhou!!!")
    elif escolha_jogador == 1 and escolha_computador == 0:
        print("Você ganhou!!! :)")
    else:
        print("Você perdeu!!! :(")


def main():
    escolha_jogador = int(input("Qual você escolhe? Digite 0 para Pedra, 1 para Papel or 2 para Tesoura...: "))
    valida_escolha_jogador(escolha_jogador)
    print(f'\nVocê escolheu:{lista_imagens[escolha_jogador]}')

    escolha_computador = random.randint(0, 2)
    print(f'\nComputador escolheu:{lista_imagens[escolha_computador]}')

    verifica_vencedor(escolha_jogador, escolha_computador)

    jogar_novamente()


if __name__ == "__main__":
    main()
