print("Determinar, de N cantidades, cuántas son menores o iguales a cero \ny cuántas mayores a cero.")

tot = 0
con = 1
num = 0
may = 0
men = 0

tot = int(input("Introduce las cantidades totales:  "))
for con in range(1,tot +1):
    num = float(input(f"Introduce la cantidad número {con}: "))
    if num <= 0:

        men += 1
    else:
        may += 1

 


print("Números mayores: ", may, "\nNúmeros menores o iguales a 0:  ", men)