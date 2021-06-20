import random
from os import SCHED_OTHER, system
from typing import List


with open('./files/data.txt', 'r', encoding='utf-8') as file:
    WORDS = [word.replace('\n','') for word in file]
VOCALS = {'Á':'A','É':'E','Í':'I','Ó':'O','Ú':'U'}


def random_word(): 
    word = list(random.choice(WORDS).upper())
    return word


word = random_word()
lines = list('-'*len(word))


def vocals_check(letter):
    n = 0
    for l in word:
        for v, vocal in VOCALS.items():
            if v == l:
                if vocal == letter:
                    n += 1
    if n > 0: return True


def main():
    system('clear')
    print('''
+-+-+-+- Bienvenido(a) al juego del ahorcado! +-+-+-+-

Instrucciones: adivinar la palabra, letra por letra!
''')
    score = 0
    choice = 1
    while choice == 1:
        word = random_word()
        lines = list('-'*len(word))
        lives = 5
        hearts = ['♥','♥','♥','♥','♥','♥']
        while lines != word and lives >= 0:
            print(f'\nVidas: {" ".join(hearts)}\n\n{" ".join(lines)}')
            #print(word) #Borrar el '#' para imprimir la palabra a adivinar
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
            except TypeError: print('\nDebes ingresar una letra!')
            except AssertionError: print('\nDebes ingresar una letra!')
        try:
            if lines == word:
                system('clear')
                score += 1
                print(f'\nVidas: {" ".join(hearts)}\n\nHaz adivinado la palabra {"".join(word)}!\n\nPuntaje: {score}')
                choice = int(input('\n1. Seguir jugando\n2. Salir \nElija una opcion: '))
            else:
                system('clear')
                score -= 1
                print(f'\nVidas: {" ".join(hearts)}\n\nHaz perdido, la palabra era {"".join(word)}\n\nPuntaje: {score}')
                choice = int(input('\n1. Seguir jugando\n2. Salir \nElija una opcion: '))
        except ValueError: choice = int(input('\n1. Seguir jugando\n2. Salir \nPor favor, elija una opcion valida: '))


if __name__ == '__main__':
    main()