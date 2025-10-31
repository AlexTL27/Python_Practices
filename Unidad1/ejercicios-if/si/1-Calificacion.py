print("Aplicación que lea 7 calificaciones, calcule el promedio  y si es mayor a 8 que lo imprima")

c1 = int(input("Ingresa la calificación 1:  "))
c2 = int(input("Ingresa la calificación 2:  "))
c3 = int(input("Ingresa la calificación 3:  "))
c4 = int(input("Ingresa la calificación 4:  "))
c5 = int(input("Ingresa la calificación 5:  "))
c6 = int(input("Ingresa la calificación 6:  "))
c7 = int(input("Ingresa la calificación 7:  "))

prom = (c1+c2+c3+c4+c5+c6+c7) / 7


if prom > 8:
    print("Aprobado  ", "\nPromedio:  ", prom)

else:
    print("Reprobado  ", "\nPromedio:  ", prom)
  



