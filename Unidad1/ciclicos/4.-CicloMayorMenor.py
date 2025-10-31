#####Hecho por Alex Efrén Téllez Limón#####

print("Aplicación para determinar, de N cantidades, cuántas son menores o iguales a cero y cuántas mayores a cero.")

con = 1

tot = int(input("Ingresa las cantidades a revisar:  "))

while con <= tot:
    print("Ingresa el digito número ", con)
    num = float(input())

    if num <= 0:
        print("El número es menor o igual a cero")
    else: 
        print("El número es mayor a cero")
    
    con+=1
    


 

    