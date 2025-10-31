print("Aplicación que lea el nombre, año de nacimiento, año actual y si es mayor de 18 años imprima el nombre y eres mayor de edad")

nom = input("Ingresa tu nombre: ")

nac = int(input("Ingresa el año de nacimiento:  "))

if 2025 - nac >= 18:
    print(nom,",eres o estas por ser mayor de edad")