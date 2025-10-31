#####Hecho por Alex Efrén Téllez Limón#####

print("Aplicación para determinar cuánto se debe pagar por equis cantidad de lápices considerando que si son 1000 o más el costo es de 85¢; de lo contrario, el precio es de 90¢.")

lap = int(input("Indica la cantidad de lápices:  "))

if lap >= 1000:
    print("$85")
else:
    print("$95")