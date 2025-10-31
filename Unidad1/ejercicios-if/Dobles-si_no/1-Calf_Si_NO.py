#####Hecho por Alex Efrén Téllez Limón#####

print("aplicación que lea 8 calificaciones, muestre el promedio y si es mayor a 8 muestre el mensaje aprobado, de lo contrario indicar reprobado")

c1 = int(input("Ingresa la calificación 1:  "))
c2 = int(input("Ingresa la calificación 2:  "))
c3 = int(input("Ingresa la calificación 3:  "))
c4 = int(input("Ingresa la calificación 4:  "))
c5 = int(input("Ingresa la calificación 5:  "))
c6 = int(input("Ingresa la calificación 6:  "))
c7 = int(input("Ingresa la calificación 7:  "))
c8 = int(input("Ingresa la calificación 8:  "))


prom = (c1+c2+c3+c4+c5+c6+c7+c8) / 8


if prom > 8:
    print("Aprobado  ", "\nPromedio:  ", prom)

else:
    print("Reprobado  ", "\nPromedio:  ", prom)