#####Hecho por Alex Efrén Téllez Limón#####

print("El consultorio del Dr. Lorenzo T. Mata Lozano tiene como política cobrar la consulta con base en el número de cita, de la siguiente forma: Las tres primeras citas a $200.00 c/u. Las siguientes dos citas a $150.00 c/u. Las tres siguientes citas a $100.00 c/u. Las restantes a $50.00 c/u, mientras dure el tratamiento. Se requiere un algoritmo para determinar: Cuánto pagará el paciente por la cita. El monto de lo que ha pagado el paciente por el tratamiento.")

cita = 0
total = 0



num = int(input("Introduce el número de cita:  "))
con = num

#cita es el total pagado, total es lo que se pago de la ultima cita
if num >= 1:
    cita += 200
    total = 200
    con-=1

if num >= 2:
    cita += 200
    con-=1

if num >= 3:
    cita += 200
    con-=1

if num >= 4:
    cita += 150
    total = 150
    con-=1
    
    
if num >= 5:
    cita += 150
    con-=1

if num >= 6:
    cita += 100
    total = 100
    con-=1

if num >= 7:
    cita += 100
    con-=1
   
if num >= 8:
    cita += 100
    con-=1


if num >= 9:
    cita += 50 * con
    total = 50

 
 
        
        


print("Costo de la cita:  ", total)

print("Total pagado: ", cita)


