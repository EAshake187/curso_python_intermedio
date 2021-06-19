def divisors(num):
    divisors = []
    for i in range(1,num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def main():

    num = input('Ingresa un numero: ')
    assert num.isnumeric() and int(num) > 0, 'Debes ingresar un numero' #Evalúa una condicional, si esta se cumple continuamos con el flujo normal del python, si no se cumple eleva un error del tipo AssertionError
    print(divisors(int(num)))
    print('Termino el programa')


if __name__ == '__main__':
    main()