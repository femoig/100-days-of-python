'''
Loops with Range
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
            senha += letras_maiusculas[random.randint(0, len(letras_maiusculas) - 1)]
        elif ultimo_digito:
            senha += caracteres_especiais[random.randint(0, len(caracteres_especiais) - 1)]
        else:
            senha += letras_minusculas[random.randint(0, len(letras_minusculas) - 1)]
    return senha


def main():
    print("Gerador de senhas!")
    size = int(input("Qual o tamanho da senha que deseja criar?...: "))
    senha = generate_password(size)
    print(f"Sua senha é: {senha}")


if __name__ == "__main__":
    main()
