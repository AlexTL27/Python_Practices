def Trapecioarea():

 baseMa = int(input("Ingresa el valor de la base Mayor:  "))
 baseMe = int(input("Ingresa el valor de la base Menor:  "))
 altura = int(input("Ingresa el valor de la altura: "))

 area = ((baseMa + baseMe) * altura) / 2
 return area

#################Pentagono############################
def Pentagonoarea():

 lado = float(input("Ingresa el valor de lado: "))
 apotema = float(input("Ingresa el valor del apotema: "))

 
 p = lado * 5
 return (p * apotema) / 2
    

################Triangulo#########################
def Trianguloarea():
 
 base = int(input("Ingresa el valor de la base: "))
 altura = int(input("Ingresa el valor de la altura: "))



 return (base * altura) / 2



 ################Circulo######################
def Circuloarea():
     

 radio = int(input("Ingresa el valor del Radio: "))
 PI = 3.1416

 #######Resultado############
 return PI  * (radio ** 2)






###############Cuadrado######################
def Cuadradoarea():
   
 lado = int(input("Ingresa el valor de el lado: "))


 #######Resultado############
 return lado * lado  
 


while(True):
 print("Indica la figura que quieres obtener su área \n1.-Trapecio\n2.-Pentagono\n3.-Tríangulo\n4.-Círculo\n5.-Cuadrado")
 val = int(input("Introduce la acción a realizar:  "))
 

 match val:
     case 1:
          print(Trapecioarea())
     case 2:
          print(Pentagonoarea())
     case 3:
          print(Trianguloarea())
     case 4:
          print(Circuloarea())
     case 5:
          print(Cuadradoarea())
     case _:
       print("Opción no válida")
       continue
        
  
