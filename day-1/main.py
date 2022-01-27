def main():
    print('Hello World')

def say_name():
    name = input("Qual seu nome? ")
    print(f'Hello {name}!')
    print(f'Seu nome tem um tamanho de {len(name)}')

if __name__ == '__main__':
    say_name()
