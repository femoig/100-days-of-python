'''
Caeser Cipher

arguments, parameters, functions and input
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

def caeser_method(start_text, shift, direction):
    end_text = ""

    if direction.lower == "decode":
        shift *= -1

    for letra in start_text:
        position = alphabet.index(letra)
        new_position = position + shift
        new_letra = alphabet[new_position]
        end_text += new_letra
    print(f"Output text is...: {end_text}")

# def encrypt(text, shift):
#     encoded_text = ""
#     for letra in text:
#         position = alphabet.index(letra)
#         new_position = position + shift
#         new_letra = alphabet[new_position]
#         encoded_text += new_letra
#     print(f"Encoded text is...: {encoded_text}")
#
# def decrypt(text, shift):
#     decoded_text = ""
#     for letra in text:
#         position = alphabet.index(letra)
#         new_position = position - shift
#         new_letra = alphabet[new_position]
#         decoded_text += new_letra
#     print(f"Decoded text is...: {decoded_text}")

def main():
    print("Caeser Cipher - Encode/Decode")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caeser_method(text, shift, direction)

    # if direction.lower() == "encode":
    #     encrypt(text, shift)
    # else:
    #     decrypt(text, shift)


if __name__ == "__main__":
    main()

