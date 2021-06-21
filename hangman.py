import random
from os import SCHED_OTHER, system
from typing import List

############ Leyendo el archivo con las palabras ############
with open('./files/data.txt', 'r', encoding='utf-8') as file:
    WORDS = [word.replace('\n','') for word in file]


############ Selecciona una palabra al azar ############
def random_word(): 
    word = list(random.choice(WORDS).upper())
    return word
word = random_word()

############ Corrije palabras acentuadas ############
VOCALS = {'Á':'A','É':'E','Í':'I','Ó':'O','Ú':'U'}
def vocals_check(letter):
    n = 0
    for l in word:
        for v, vocal in VOCALS.items():
            if v == l:
                if vocal == letter:
                    n += 1
    if n > 0: return True

############ Fases del hangman ############
hangman = {0:'''
+-+---+
  |   |
  0   |
 /|\  |
 / \  |
      |
=========
''',1:'''
+-+---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',2:'''
+-+---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',3:'''
+-+---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',4:'''
+-+---+
  |   |
  O   |
  |   |
      |
      |
=========
''',5:'''
+-+---+
  |   |
  O   |
      |
      |
      |
=========
''',6:'''
+-+---+
  |   |
      |
      |
      |
      |
=========
''',7:'''
+-+---+
  |   |
      |
 \O/  |
  |   |
 / \  |
=========
'''}

############ Sistema principal del juego ############
def main():
    score = 0
    choice = 1
    while choice == 1:
        word = random_word() #Selecionando palabra al azar
        lines = list('-'*len(word)) #Ocultando la palabra
        lives = 5
        hearts = ['♥','♥','♥','♥','♥','♥']
        while lines != word and lives >= 0: #Mientras que la palabra oculta no se parezca a la palabra o las vidas no se acaben
            system('clear')
            print('''
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                 by: Edgaralfon
+-+-+-+-+-+-+ Bienvenido(a) al juego del ahorcado! -+-+-+-+-+-+-

    INSTRUCCIONES: adivinar la palabra, letra por letra!

-+-+-+-+-+-+--+-+-+-+-+-+--+-+-+-+-+-+--+-+-+-+-+-+--+-+-+-+-+-+''')
            print(f'\nVidas: {" ".join(hearts)} | Puntaje:{score}{hangman[lives+1]}\n{" ".join(lines)}')
            #print(word) #Borrar el '#' para imprimir la palabra a adivinar
            try:
                letter = input('Ingresa una letra: ').upper() #Una letra ingresada por el usuario
                assert len(letter) > 0 #En caso de que no se ingrese nada
                if letter.isnumeric():
                    raise TypeError #En caso de que se ingrese un numero
                if letter in word or (vocals_check(letter)): #Si la palabra contiene la letra o la letra acentuada
                    for i, l in enumerate(word): #Comparacion
                        if l in VOCALS: #Arreglando vocales acentuadas
                            l = VOCALS.get(l)
                        if l == letter:
                            lines[i] = word[i] #Intercambiando la letra ingresada por el espacio correspondiente en la palabra oculta
                else: #En caso de no adivinar ninguna letra
                    hearts[lives] = '♡'
                    lives -= 1
            except TypeError: pass
            except AssertionError: pass
        try:
            if lines == word: #Si la palabra es adivinada
                system('clear')
                print('''
 ██████╗ ██████╗ ███╗   ██╗ ██████╗ ██████╗  █████╗ ████████╗███████╗██╗
██╔════╝██╔═══██╗████╗  ██║██╔════╝ ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
██║     ██║   ██║██╔██╗ ██║██║  ███╗██████╔╝███████║   ██║   ███████╗██║
██║     ██║   ██║██║╚██╗██║██║   ██║██╔══██╗██╔══██║   ██║   ╚════██║╚═╝
╚██████╗╚██████╔╝██║ ╚████║╚██████╔╝██║  ██║██║  ██║   ██║   ███████║██╗
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
-+-+-+-+-+-+--+-+-+-+-+-+--+-+-+-+-+-+--+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+''')
                score += 1
                print(f'\nVidas: {" ".join(hearts)} | Puntaje:{score}{hangman[7]}\nHaz adivinado la palabra {"".join(word)}!')
                choice = int(input('\n1. Seguir jugando\n2. Salir \nElija una opcion: '))
            else: #Si la palabra no se adivina
                system('clear')
                print('''
 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ ██╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗██║
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝██║
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗╚═╝
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║██╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝             
-+-+-+-+-+-+--+-+-+-+-+-+--+-+-+-+-+-+--+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-''')
                score -= 1
                print(f'\nVidas: {" ".join(hearts)} | Puntaje:{score}{hangman[lives+1]}\nHaz perdido, la palabra era {"".join(word)}')
                choice = int(input('\n1. Seguir jugando\n2. Salir \nElija una opcion: '))
        except ValueError: choice = int(input('\n1. Seguir jugando\n2. Salir \nPor favor, elija una opcion valida: '))


if __name__ == '__main__':
    main()