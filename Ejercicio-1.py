"""
    Ejercicio #1:

        Una juguetería tiene mucho éxito en dos de sus productos: payasos y
        muñecas. Suele hacer venta por correo y la empresa de logística les cobra
        por peso de cada paquete así que deben calcular el peso de los payaso y 
        muñecas que saldrán en cada paquete a demanda. Cada payaso tiene un peso de
        112g y cada muñeca de 75g. 
        
        Escribe un programa que lea el número de payasos y muñecas vendidos en el último
        pedido y calcule el peso total del paquete que será enviado.
"""

total_payasos = int(input('Ingrese la cantidad total de payasos: '))
total_munecas = int(input('Ingrese la cantidad total de muñecas: '))

peso_payasos = total_payasos*112
peso_munecas = total_munecas*75
total = peso_payasos + peso_munecas

print('El peso total del paquete es de: ' + str(total))
print('El peso total del paquete es de: {}'.format(total))
print(f'El peso total del paquete es de: {total}')