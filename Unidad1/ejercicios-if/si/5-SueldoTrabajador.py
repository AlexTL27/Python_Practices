print("Dado el sueldo de un trabajador, aplica un aumento del 15% ","si su sueldo es iferior a 3000, e imprime el nuevo sueldo")

sueldoTrabajador = float(input("Ingresa el sueldo: "))

if sueldoTrabajador < 3000:
    bono = sueldoTrabajador * .15
    sueldoBono =  sueldoTrabajador + bono
    print("El nuevo sueldo es de:  ", sueldoBono)

