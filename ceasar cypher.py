alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
accepted_input = ['encode', 'decode']


def morph_text(text, shift, direction):
    result = ''
    for letter in text:
        if letter in alphabet:
            letter_position = alphabet.index(letter)
            if direction == 'decode':
                result += alphabet[letter_position - shift]
            else:
                if (letter_position) + shift > 26:
                    j = (letter_position - 26) + shift
                    result += alphabet[j]
                else:
                    result += alphabet[letter_position + shift]
        else:
            result += letter
    return result


keep_playin = True

while keep_playin:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction not in accepted_input:
        print('invalid input.\n')
        continue

    text = input("Type your message:\n").lower()

    try:
        shift = int(input("Type the shift number:\n"))
        if shift > 26:
            shift = shift % 26
    except Exception:
        print('invalid input.\n')
        continue

    print(morph_text(text, shift, direction))

    if input('Again?[y/n]\n') == 'n':
        keep_playin = False
