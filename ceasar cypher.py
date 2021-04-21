import operator

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if shift > 26:
    shift = shift % 26


def encrypt(text, shift):
    result = ''
    for letter in text:
        if letter in alphabet:
            letter_position = alphabet.index(letter)

            if (letter_position) + shift > 26:
                j = (letter_position - 26) + shift
                result += alphabet[j]
            else:
                result += alphabet[letter_position + shift]
        else:
            result += letter
    return result


def decrypt(text, shift):
    result = ''
    for letter in text:
        if letter in alphabet:
            letter_position = alphabet.index(letter)
            result += alphabet[letter_position - shift]
        else:
            result += letter
    return result


if direction == 'encode':
    print(encrypt(text, shift))
elif direction == 'decode':
    print(decrypt(text, shift))
else:
    print('input error')
