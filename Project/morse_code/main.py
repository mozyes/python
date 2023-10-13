MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

REVERSED_MORSE_CODE_DICT = {value:key for key, value in MORSE_CODE_DICT.items()}

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter.upper()] + ' '
        else:
            cipher += ' '

    return cipher


def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    space = 0
    for letter in message:
        if letter != ' ':
            space = 0
            citext += letter
        else:
            space += 1
            if space == 2:
                decipher += ' '
            else:
                decipher += REVERSED_MORSE_CODE_DICT.get(citext, '?')
                citext = ''

    return decipher

def main():
    message = input('Give your sentence: ')
    choice = input('What do you want to do?("encrypt/decrypt"): ')
    if choice.lower() == 'encrypt':
        result = encrypt(message)
    else:
        result = decrypt(message)
    print(result)


main()
