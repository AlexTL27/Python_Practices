print("Elige un producto: \n1.-Refrescos: 12\n2.-Agua Mineral: 8\n3.-Galletas emperador: 12\n4.-Maruchan: 10")

op = input()
prod = ""
prec = 0
bandera = False
cant = -1

match op:
 case "1":
  prod = "Refresco"
  prec = 12
 case "2":
  prod = "Agua Mineral"
  prec = 8
 case "3":
  prod = "Galletas Emperador"
  prec = 12
 case "4":
  prod = "Maruchan"
  prec = 10

 case _:
  print("Opción no válida")
  bandera = True
       

if bandera == False:
 while cant < 0:
    print("Indica la cantidad, no se acepta menor a 0")
    cant = float(input())
    

print(prod, "Precio: ", prec, " Cantidad: ", cant, "Total: ", cant * prec)