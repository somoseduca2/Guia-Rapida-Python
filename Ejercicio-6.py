"""
    Ejercicio #6:
        Escribir una función que calcule el área de un círculo
        y otra que calcule el volumen de un cilindro usando
        la primera función.

        Área de un círculo: Ac = Pi * (radio**2)
        Volumen de un cilindro: Aci = Pi * (radio**2) * h
"""

pi = 3.1416
def area_circulo(radio):
    area = pi * (radio**2)
    return area

def volumen_cilindro(radio, h):
    volumen = area_circulo(radio) * h
    return volumen

resultado_circulo = area_circulo(5)
resultado_cilindro = volumen_cilindro(10, 15)

print(resultado_circulo, resultado_cilindro)
