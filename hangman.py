import random
from os import system
from typing import List


with open('./files/data.txt', 'r', encoding='utf-8') as file:
    WORDS = [word.replace('\n','') for word in file]
word = list(random.choice(WORDS).upper())
lines = list('-'*len(word))
VOCALS = {'Á':'A','É':'E','Í':'I','Ó':'O','Ú':'U'}
lives = 5
hearts = ['♥','♥','♥','♥','♥','♥']


def vocals_check(letter):
    n = 0
    for l in word:
        for v, vocal in VOCALS.items():
            if v == l:
                if vocal == letter:
                    n += 1
    if n > 0: return True


def main():
    global lives
    system('clear')
    print('''
+-+-+-+- Bienvenido(a) al juego del ahorcado! +-+-+-+-

Instrucciones: adivinar la palabra, letra por letra!
''')
    while lines != word and lives >= 0:
        print('\nVidas:',' '.join(hearts))
        print('\n',' '.join(lines))
        #print(word) #RECORDAR BORRAR
        try:
            letter = input('Ingresa una letra: ').upper()
            assert len(letter) > 0
            if letter.isnumeric():
                raise TypeError
            if letter in word or (vocals_check(letter)):
                for i, l in enumerate(word):
                    if l in VOCALS:
                        l = VOCALS.get(l)
                    if l == letter:
                        lines[i] = word[i]
            else:
                hearts[lives] = '♡'
                lives -= 1
        except TypeError: print('Debes ingresar una letra!\n')
        except AssertionError: print('Debes ingresar una letra!\n')
    if lines == word:
        print('\nVidas:',' '.join(hearts))
        print(f'\nHaz adivinado la palabra {"".join(word)}!')
    else:
        print('\nVidas:',' '.join(hearts))
        print(f'\nHaz perdido, la palabra era {"".join(word)}')


if __name__ == '__main__':
    main()