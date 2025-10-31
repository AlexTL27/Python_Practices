print("Determinar cuánto ahorrará una persona en un año\nsi al final de cada mes deposita x cantidad de dinero\nademás, se requiere saber cuánto lleva ahorrado cada mes.")

tot = 0
con = 1
sum = 0

while con <= 12:
    sum = float(input(f"Cuanto introduciras el mes número {con}: "))
    tot += sum
    con += 1
    print("Ahorrado hasta el momento:  ", tot)


print("Ahorrado en un año:  ", tot)