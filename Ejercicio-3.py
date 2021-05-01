"""
    Ejercicio #3:
        Cree un programa que tome como entrada la hora exacta
        (hora, minutos, segundos y AM/PM) e indique el número de segundos
        transcurridos durante ese día.
"""

horas = int(input('Hora: '))
minutos =int(input('Minutos: '))
segundos = int(input('Segundos: '))
am_pm = input('AM/PM: ')

total_segundos = 0

if am_pm == 'am' or am_pm == 'AM' or am_pm == 'aM' or am_pm == 'Am':
    total_segundos = horas * 3600
    # total_segundos = total_segundos + (minutos * 60)
    # total_segundos = total_segundos + segundos
    total_segundos += (minutos*60)
    total_segundos += segundos
elif am_pm == 'pm' or am_pm == 'PM' or am_pm == 'pM' or am_pm == 'Pm':
    total_segundos = 12*3600 # 43200
    total_segundos += (horas * 3600)
    total_segundos += (minutos*60)
    total_segundos += segundos
else:
    print('Valor de entrada incorrecto (AM/PM)')

print(f'La cantidad total de segundos transcurridos es de: {total_segundos}')