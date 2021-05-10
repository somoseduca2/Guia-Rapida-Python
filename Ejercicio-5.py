"""
    Ejercicio #5:
        Escriba un programa que calcule el valor aproximado de PI usando la serie:
            
            PI = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - ... +- (4/N)

        Considere que el valor N será indicado por el usuario. 
"""

n = 99999
resultado = 0.0
iteracion = 0

for i in range(1, n+1, 2):
    if iteracion % 2 == 0:
        resultado += (4/i)
    else:
        resultado -= (4/i)
    iteracion += 1

print(f'La aproximacion de PI es: {resultado}')