print("Esta aplicación indica si un número es primo o no")


bandera = False
num = int(input("Introduce un número:  "))

for a in range(2,num):
    

    if num % a == 0:
        bandera = True
    if bandera:
        break


if not bandera :
    print("El número es primo")
else:
    print("El número es compuesto")

