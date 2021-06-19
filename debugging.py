def divisors(num):
    divisors = []
    for i in range(1,num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def main():

    try: #se coloca código que esperamos que pueda lanzar algún error.
        num = int(input('Ingresa un numero: '))

        if num <= 0: 
            raise ValueError #Nos permite generar errores, es decir crear nuestros propios errores cuando detectemos que nuestro programa no actúa como debería con cierto tipo de datos
        print(divisors(num))

    except ValueError: #se maneja el error, es decir, si ocurre un error dentro del bloque de código del try, se deja de ejecutar el código del try y se ejecuta lo que se haya definido en el Except.
        print('Debes ingresar un numero entero positivo')

    finally: #Se ejecuta exista un error o no, no es muy usual pero puede darse para cerrar archivos, conexiones a BBDD o liberar recursos
        print('Termino el programa')


if __name__ == '__main__':
    main()