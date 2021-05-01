"""
    Ejercicio #2:
        Realice un programa que reciba como entrada un número entre 1 y 12 e imprima
        el nombre del mes correspondiente. Tome en cuenta posibles valores erróneos 
        en la entrada.
"""

numero = int(input('Ingrese un número de mes que desee: '))

if numero >= 1 and numero <= 12:
    if numero == 1:
        print('Enero')
    elif numero == 2:
        print('Febrero')
    elif numero == 3:
        print('Marzo')
    elif numero == 4:
        print('Abril')
    elif numero == 5:
        print('Mayo')
    elif numero == 6:
        print('Junio')
    elif numero == 7:
        print('Julio')
    elif numero == 8:
        print('Agosto')
    elif numero == 9:
        print('Septiembre')
    elif numero == 10:
        print('Octubre')
    elif numero == 11:
        print('Noviembre')
    elif numero == 12:
        print('Diciembre')
else:
    print('Ha ingresado un valor incorrecto')
