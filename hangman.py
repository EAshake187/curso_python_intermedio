import random
from os import system


WORDS = []
with open('./files/data.txt', 'r', encoding='utf-8') as file:
    WORDS = [word.replace('\n','') for word in file]
word = list(random.choice(WORDS).upper())
lines = list('-'*len(word))


def comparison(letter):
    global word
    global lines
    for l in range(0,len(word)):
        if word[l] == letter:
            lines[l] = letter


def main():
    system('clear')
    print('''
+-+-+-+- Bienvenido(a) al juego del ahorcado! +-+-+-+-

Instrucciones: adivinar la palabra, letra por letra!
''')
    #print(word)
    while lines != word:
        print('\n',' '.join(lines))
        try:
            letter = input('Ingresa una letra: ').upper()
            assert len(letter) > 0
            if letter.isnumeric():
                raise TypeError
            comparison(letter)
        except TypeError: print('Debes ingresar una letra!\n')
        except AssertionError: print('Debes ingresar una letra!\n')
    if lines == word:
        print(f'\nHaz adivinado la palabra {"".join(lines)}!')


if __name__ == '__main__':
    main()