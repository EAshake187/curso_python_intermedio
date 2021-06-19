from os import EX_CONFIG


def read():
    numbers = []
    with open('./files/numbers.txt', 'r', encoding='utf-8') as file:
        for line in file:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ['Edgar', 'Miguel', 'Cristian', 'Facundo', 'Rocío']
    with open('./files/names.txt', 'w', encoding='utf-8') as file:
        for name in names:
            file.write(name)
            file.write('\n')


def main():
    write()


if __name__ == '__main__':
    main()