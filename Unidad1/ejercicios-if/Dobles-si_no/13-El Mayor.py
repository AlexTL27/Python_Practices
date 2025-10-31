#####Hecho por Alex Efrén Téllez Limón#####

print("Aplicación la cual tras leer 3 valores permita determinar cuál es el mayor de los 3, desarrollar el algoritmo o seudocódigo y el diagrama de flujo.")

n1 = float(input("Indica el primer dígito:  "))
n2 = float(input("Indica el segundo dígito:  "))
n3 = float(input("Indica el tercer dígito:  "))


if n1 > n2:
    if  n1 > n3:
         print(n1)
    else:
        print(n3)
elif n2 > n3:
    print(n2) 
else:
    print(n3)

 


  
