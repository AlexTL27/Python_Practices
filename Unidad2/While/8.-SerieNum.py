print("Pulsa numeros, cuando se teclee uno negativo saldras, al final se mmostraran cuales y cuantos has introducido.")

cad = "//"
num = 1
con = 0
while True:
   
    num = float(input("Introduce un número:  "))
    if num < 0:
      break
    cad += str(num) + "//"
    con += 1
    
print("Números introducidos:", cad, "\nEl total de números introducidos es: ", con)