#####Hecho por Alex Efrén Téllez Limón#####

print("Aplicación para obtener la suma de diez cantidades mediante la utilización de un ciclo.")

con = 1
res = 0

while con <= 10:
    print("Indica el digito numero", con)
    suma = float(input())

    res = res + suma

    con+=1 #con igual al valor de con + 1

    print("Obtenido hasta el momento:  ", res)

print("Resultado:  ", res) 


