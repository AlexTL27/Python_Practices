print("Determinar cuánto ahorrará una persona en un año\nsi al final de cada mes deposita x cantidad de dinero\nademás, se requiere saber cuánto lleva ahorrado cada mes.")

tot = 0
con = 1
sum = 0

for con in  range(1,13):
    sum = float(input(f"Cuanto introduciras el mes número {con}: "))
    tot += sum

    print("Ahorrado hasta el momento:  ", tot)


print("Ahorrado en un año:  ", tot)