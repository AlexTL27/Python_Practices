print("el hijo de Doña Luisa mide 6 pies y 2 pulgadas. Crea una aplicación que convierta a metros")

ft = float(input("Ingresa la medida en pies:  "))

pul = float(input("Ingresa la medida en pulgadas:  "))
 

mul = (ft * 12) * 2.54

ft = mul / 100

ft = ft + (pul * 2.54 ) / 100

print("Total:  ", ft)