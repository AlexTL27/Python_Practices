#####Hecho por Alex Efrén Téllez Limón#####

print("Aplicación que lea 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si no que los sume.")

n1 = float(input("Ingresa el primer número:  "))
n2 = float(input("Ingresa el segundo número:  "))

if n1 == n2:
    print("Multiplicación:  ", n1 * n2 )
elif n1 > n2:
      print("Resta:  ", n1 - n2 )
else:
       print("Suma:  ", n1 + n2 )
