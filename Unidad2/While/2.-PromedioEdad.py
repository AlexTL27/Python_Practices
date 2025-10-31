print("Edad promedio de un grupo de N alumnos.")

sum = 0
con = 1
calf = 0


alum = int(input("Introduce los alumnos totales:  "))

while con <= alum:
    calf = int(input(f"Introduce el alumno número {con}:  "))
    sum += calf
    con += 1


print("Resultado:  ", sum / alum)