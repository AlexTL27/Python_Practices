#####Hecho por Alex Efrén Téllez Limón#####

print("Aplicación para determinar cuánto ahorrará una persona en un año, si al final de cada mes deposita variables cantidades de dinero; además, se requiere saber cuánto lleva ahorrado cada mes.")

tot = 0
con = 1


while con <= 12:
     print("Ingrese la cantidad de dinero que \nAhorrara en el mes",con)
     sum = int(input())
     tot += sum #tot igual a tot + sum
     con += 1

     print("Ahorrado hasta el momento: ", tot)

print("Ahorrado en un año: ", tot)

