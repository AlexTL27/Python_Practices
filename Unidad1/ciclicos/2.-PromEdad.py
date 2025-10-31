#####Hecho por Alex Efrén Téllez Limón#####

print("Aplicación para obtener la edad promedio de un grupo de N alumnos.")

alum = int(input("Ingrese la cantidad de Alumnos: "))
con = 1
sum = 0
while con <= alum :
    print("Ingrese la calificación número ",con)
    calf = int(input())

    sum = sum + calf

    con+=1

print("Resultado:  ", sum/alum)