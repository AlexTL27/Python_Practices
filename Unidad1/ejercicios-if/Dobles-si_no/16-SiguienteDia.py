#####Hecho por Alex Efrén Téllez Limón#####

print("Pedir el día, mes y año de una fecha correcta y mostrar la fecha del día siguiente. Suponer que todos los meses tienen 30 días.")

dia = int(input("Ingresa el número del día:  "))

mes = int(input("Ingresa el número del mes:  "))

year = int(input("Ingresa el año:  "))

dia += 1

if dia == 31:
    dia = 1
    mes += 1

    if mes == 13:
        year += 1
        mes = 1

print("Año:  ", year,"  Mes:  ", mes, "  Día:  ", dia)


