#####Hecho por Alex Efrén Téllez Limón#####

print("Se esta organizando un viaje, si son 100 alumnos o más el costo es de $65 c/u, 50-99 $70 c/u, 30-49 $95 c/u, menos de 30 4000 por todos")

per = int(input("Ingresa la cantidad de alumnos:  "))

if per >= 100:
    print("$65 c/u")
elif per >= 50 and per <= 99:
     print("$70 c/u")
elif per >= 30 and per <= 49:
     print("$95 c/u")
else:
     print("4000 por todos")