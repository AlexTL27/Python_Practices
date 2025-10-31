#####Hecho por Alex Efrén Téllez Limón#####

print("Aplicación que tras leer 2 valores cumpla las siguientes condiciones. 1.- Si son los números iguales que los sume. 2.- Si el primer valor es mayor al segundo que realice una resta. 3.- Si el segundo es mayor al primer valor que realice una multiplicación.")

n1 = float(input("Indica el primer dígito:  "))
n2 = float(input("Indica el segundo dígito:  "))

if n1 > n2:
    print("Resta:  ", n1 - n2)
elif n2 > n1:
     print("Multiplicación:  ", n1 * n2)
else: 
      print("Suma:  ", n1 + n2)

