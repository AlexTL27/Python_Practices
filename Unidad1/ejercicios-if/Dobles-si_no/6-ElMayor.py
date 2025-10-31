#####Hecho por Alex Efrén Téllez Limón#####

print("Aplicación que lea dos números y que muestre un mensaje indicando cual es el mayor.")

num1 = int(input("Ingresa el primer número:  "))
num2 = int(input("Ingresa el segundo número:  "))

if num1 > num2:
    print(num1," Es mayor")
elif num2 > num1:
    print(num2," Es mayor")
else:
    print("Los números son iguales")