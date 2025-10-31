#####Hecho por Alex Efrén Téllez Limón#####

print("Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera: Si trabaja 40 horas o menos se le paga a $16 por hora. Si trabaja más de 40 horas se le paga a 16 por cada una de las primeras 40 horas y $20 por cada hora extra.")

hrs = int(input("Ingresa las horas trabajadas:  "))

if hrs <= 40:
    print("Total:  ",hrs * 16)
else:
    suma = 40 * 16
    hrsPos =  hrs - 40
    hrs=hrsPos * 20
    print("Total:  ",hrs + suma)