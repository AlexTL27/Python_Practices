#####Hecho por Alex Efrén Téllez Limón#####

print("Almacenes “El harapiento distinguido” tiene una promoción: a todos los trajes que tienen un precio superior a $2500.00 se les aplicará un descuento de 15 %, a todos los demás se les aplicará sólo 8 %. ")

pre = int(input("Indica el precio del traje:  "))


if pre >= 2500:
    print(pre * .15)
else:
    print(pre * .08)