'''
Functions, while loops
'''


def main():
    word = input("Digite uma palavra...: ")
    counter = 0
    while counter < len(word):
        print(word[counter].upper())
        counter += 1
    quit()


if __name__ == "__main__":
    main()