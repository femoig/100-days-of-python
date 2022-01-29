'''
Loops with Range, Random choice
'''
import random

letras_minusculas = ["a", "b", "c", "d", "e", "f"]
letras_maiusculas = ["A", "B", "C", "D", "E", "F"]
caracteres_especiais = ["!", "#", "*"]


def generate_password(size):
    senha = ""
    for position in range(0, size):
        ultimo_digito = (position == size - 1)
        primeiro_digito = (position == 0)

        if primeiro_digito:
            senha += random.choice(letras_maiusculas)
        elif ultimo_digito:
            senha += random.choice(caracteres_especiais)
        else:
            senha += random.choice(letras_minusculas)
    return senha


def main():
    print("Gerador de senhas!")
    size = int(input("Qual o tamanho da senha que deseja criar?...: "))
    senha = generate_password(size)
    print(f"Sua senha é: {senha}")


if __name__ == "__main__":
    main()
