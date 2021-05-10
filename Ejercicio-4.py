"""
    Ejercicio #4:
        Haga un programa que lea números enteros positivos de teclado, hasta que el usuario ingrese
        el número cero (0) e informar cuál fue el mayor y el menor número ingresado.

        Ejemplo:
            3
            4
            5
            1
            2
            0
            Mayor número ingresado: 5
            Menor número ingresado: 1
"""
numero = int(input('ingrese un número: '))
mayor = numero
menor = numero

while(numero != 0):
    if numero > mayor:
        mayor = numero
    
    if numero < menor:
        menor = numero
    numero = int(input('Ingrese otro número: '))

print(f'Mayor número ingresado {mayor}')
print(f'Menor número ingresado {menor}')