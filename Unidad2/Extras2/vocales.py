vocal = input("Introduce una vocal:  ")

vocales = "AEIOUaeiou"
bandera = True

for a  in vocales:
    print(a)
    if a == vocal:
        bandera = False
  

if bandera == False:
    print("Vocal")