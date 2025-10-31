#####Hecho por Alex Efrén Téllez Limón#####

print("Calcular el total que una persona debe pagar en una llantera, si el precio de cada llanta es de $800 si se compran menos de 5 llantas y de $700 si se compran 5 o más.")

total = int(input("Ingresa el total de llantas:  "))

if total >= 5:
    print("Total:  ", total * 700)
else:
       print("Total:  ", total * 800)
