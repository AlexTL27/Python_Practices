palabra = input(("Ingresa una palabra:  "))

letra = input("Introduce una vocal a buscar:  ")


can = 0

vocales = "AEIOU"
bandera = True

while True:
 for a  in vocales.lower():
    if a == letra:
        bandera = False
        break

 if bandera == False:
    break
 letra = input(("Solo se aceptan vocales, intenta nuevamente: "))






for a in palabra:
    if a.lower() == letra.lower():
        can += 1


print("La palabra ",palabra," Tiene ", can , "Vocal ", letra)
 