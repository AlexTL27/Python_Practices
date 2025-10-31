#####Hecho por Alex Efrén Téllez Limón#####

print("Pedir una hora de la forma hora, minutos y segundos, y mostrar la hora en el segundo siguiente.")

hr = int(input("Introduce la hora:  "))
min = int(input("Introduce los minutos:  "))
seg = int(input("Introduce los segundos:  "))

seg += 1

print(seg)

if seg >= 60:
    seg = 0
    min += 1
    if min >= 60:
        hr += 1
        min = 0
        if hr >= 13:
            hr = 1


print("Horas:  ",hr," Minutos:  ",min, "  Segundos:  ", seg)

