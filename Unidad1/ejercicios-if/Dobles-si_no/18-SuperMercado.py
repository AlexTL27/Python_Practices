#####Hecho por Alex Efrén Téllez Limón#####

print("Si en un supermercado el cliente a la hora de pagar muestra una tarjeta cliente le dan un descuento del 5% de lo que compro y si el cliente no tiene tarjeta cliente le dan un descuento del 2%.")

total = float(input("Ingresa el total de la compra:  "))

tar = int(input("Indica 1 para usar tarjeta o cualquier otro número para negar:  "))

if tar == 1:
    var = total * 0.05
    print("Total:  ",total - var)
else: 
     var = total * 0.02
     print("Total:  ",total - var)
         


   