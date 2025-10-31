#####Hecho por Alex Efrén Téllez Limón#####

print("El náufrago satisfecho” ofrece hamburguesas sencillas, dobles y triples, las cuales tienen un costo de $20.00, $25.00 y $28.00 respectivamente. La empresa acepta tarjetas de crédito con un cargo de 5 % sobre la compra. Suponiendo que los clientes adquieren sólo un tipo de hamburguesa, realice la aplicación y diagrama de flujo para determinar cuánto debe pagar una persona por N hamburguesas.")

print("Indica tú hamburguesa: 1.- sencilla, 2.-Estar doble, 3.-triple")

num = int(input("Indica tu hamburgues:  "))

if num == 1:
    costo = 20.00
elif num == 2:
    costo = 25.00
elif num == 3:
    costo = 28

tar = int(input("Indica 1 para usar tarjeta o cualquier otra cosa para negar"))

if tar == 1:
    ext = costo * 0.5
    print("Total:  ",costo + ext)
else:
    print("Total:  ",costo)
    
    

 
  