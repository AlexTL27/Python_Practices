
bandera = False
print("Horas trabajadas de una persona")

while True:

 sueldo = float(input("Ingresa el pago por hora:  "))
 if sueldo <= 0:
   print("No puedes explotar a los trabajadores con una paga menor o igual a 0")
   bandera = True
   break
 if bandera == True:
   break
 
 
 con = 0
 tot = 0
 hrs = 0
 hrsTot = 0
 while con <  6:
    con += 1
    print("Ingresa las horas trabajadas el día:  ", con)
    hrs = float(input())
    while hrs < 0 or hrs > 25 : 
      print("Has ingresado un valor inválido, vuelve a intentar")
      print("Ingresa las horas trabajadas el día:  ", con)
      hrs = float(input())
      
    hrsTot += hrs
    tot += sueldo * hrs

 break
if not bandera:
 print("Horas totales en una semana:  ", hrsTot)
 print("sueldo Por horas trabajadas:  ", tot)