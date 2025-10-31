print("Cuánto pagara una presona por un artículo equis, considerando que tiene un descuento del 20%, y debe pagar 15% de IVA")

prod = int(input("Ingresa el precio del producto:  "))
prodIva = (prod * .15) + prod

des = prodIva * .20

print("Precio final:  ",prodIva,"\n Precio con descuento:  ", prodIva - des)