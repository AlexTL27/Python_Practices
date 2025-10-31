##30 calificaciones, cuantos sacaron 10, cuantos 9, cuantos 8, y cuantos no aprobaron, igual o menor a 7.9 reprobado

con = 1
diez = 0
nueve = 0
ocho = 0
rep = 0
calf = 0

while con <= 10:
    print("Indica la calificación del alumno número:  ", con )

    
    calf = float(input())

    while calf < 0 or calf > 10:
        print("Calificación inválida, intenta nuevamente, Alumno número: ",con)
        calf = float(input())

    if calf == 10:
        diez += 1
    elif calf >= 9:
        nueve  += 1
    elif calf >= 8:
        ocho += 1
    else:
        rep += 1
    
    con+=1




print("Alumnos con 10:  ", diez)
print("Alumnos con 9:  ", nueve)
print("Alumnos con 8:  ", ocho)
print("Alumnos reprobados:  ", rep)
