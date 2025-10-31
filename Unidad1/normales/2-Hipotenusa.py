import math as mt

print("Programa que solicite la longitud de cada cateto de un triángulo rectángulo, calcule y muestre la longitud de su hipotenusa")

c1 = float(input("Ingresa cateto 1:  "))
c2 = float(input("Ingresa cateto 2:  "))

h = mt.sqrt(((c1**2 + c2**2) ))

print(h)