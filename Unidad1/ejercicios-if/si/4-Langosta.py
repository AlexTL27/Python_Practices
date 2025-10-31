print("Una empresa vende langostas y vende banquetes, sus tarifas son las siguientes: El  costo por platillo de una persona es de $95")
print("si el numero de personas es mayor a 200 pero menor o igual a 300, el costo serade $85")
print("Para más de 300 personas el costo por platillo es de $75")


per = int(input("Ingresa la cantidad de personas:  "))

if per <= 200:
    print("El costo es de $95")
elif per > 200 and per <= 300:
    print("El costo es de $85")
else :
    print("El costo es de 75")