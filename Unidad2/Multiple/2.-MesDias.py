print("Crear una aplicación tras pedir el nombre del mes, imprima cuantos días tiene dicho mes.")

num = input("Ingresa el número del mes:  ")

match num:
    case "1": 
        print("Enero: 31 días")
    case "2": 
        print("Febrero: 29 días")
    case "3": 
        print("Marzo: 31 días")
    case "4":
        print("Abril: 30 días")
    case "5":
        print("Mayo: 31 días")
    case "6":
        print("Junio: 30 días")
    case "7":
        print("Julio: 31 días")
    case "8":
        print("Agosto: 31 días")
    case "9":
        print("Septiembre: 30 días")
    case "10":
        print("Octubre: 31 días")
    case "11":
        print("Noviembre: 30 días")
    case "12":
        print("Diciembre: 31 días")
    case _:
       print("Opción no válida")
       
    