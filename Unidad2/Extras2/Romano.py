print("Este programa imprime numeros decimales enteros a romano, máximo 3999 ")


def valor():
 num = int(input("Ingresa un número a convertir:  "))
 romano = ""
 while True:
    
    if num >= 4000: 
        print("Número inválido")
        break
    #Numero maximo
    while num >= 1000:
        num -= 1000
        romano = romano + "M"
      
    if num >= 900:
        num -= 900
        romano = romano + "CM"

    if num >= 500:
        num -= 500
        romano  = romano + "D"
     
    while num >= 400:
        num -= 400
        romano = romano + "CD"
    while num >= 100:
        num -= 100
        romano = romano + "C"
    while num >= 90:
        num -= 90
        romano = romano + "XC"
    while num >= 50:
        num -= 50
        romano = romano + "L"
    
    if num >= 40:
        num -= 40
        romano = romano + "XL"

    while num >= 10:
        num -= 10
        romano = romano + "X"
    if num == 9:
        num -=9
        romano = romano + "IX"
       
    while num >= 5:
         num -= 5
         romano = romano + "V"
    
    if num == 4:
        num -= 4
        romano = romano + "IV"
           

    while num >= 1:
        num -= 1
        romano = romano + "I"


    return romano   

while True:
 print("Conversión:  ", valor())