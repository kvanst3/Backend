import operator

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
result = []


def encrypt(text, shift):
    for letter in text:
        if letter in alphabet:
            letter_position = alphabet.index(letter)

            if (letter_position) + shift > 26:
                j = (letter_position - 26) + shift
                result.append(alphabet[j])
            else:
                result.append(alphabet[letter_position + shift])
        else:
            result.append(letter)
    return result


def decrypt(text, shift):
    for letter in text:
        if letter in alphabet:
            letter_position = alphabet.index(letter)
            result.append(alphabet[letter_position - shift])
        else:
            result.append(letter)
    return result


if direction == 'encode':
    print(''.join(encrypt(text, shift)))
elif direction == 'decode':
    print(''.join(decrypt(text, shift)))
else:
    print('input error')
