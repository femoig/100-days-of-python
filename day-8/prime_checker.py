'''
Prime Number Checker
'''

def prime_check(number):
    is_prime = True
    for n in range(2, number):
        if (number % n) == 0:
            is_prime = False

    if is_prime:
        print(f"O número {number} é primo!")
    else:
        print(f"O número {number} não é primo!")





if __name__ == "__main__":
    n = int(input("Digite um número...: "))
    prime_check(number=n)
