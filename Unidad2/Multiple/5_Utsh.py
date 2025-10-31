
print("Este programa imprime las carrera con sus respectivos encargados de la UTSH") 

print("Carreras: \n1.-Ing.en Tecnologías de la Información\n2.-Lic.en Terapia Física\n3.-Ing.en Mecatrónica\n4.-Lic.en Inovación de Negocios y Mercadotecnia")
print("5.-Ing.en Manejo Sustentable de Recursos Naturales\n6.-Ing.en Metal Mecánica\n7.-Ing.en Mantenimiento Industrial\n8.-Ing.Industrial\n9.-Lic.en Contabilidad")
print("10.-Lic.en Gestión de Capital Humano\n11.-Ing.en Diseño Textil y Moda\n12.-Lic.en Enfermería\n13.-Lic.en Cirujano Medico y Partero\n14.-Ing.Civil")

val = input("Ingrese la carrera que desea estudiar: ")

match val:
    case "1":
        print("El director del área Tecnologías de la información es el Ing.Luis Alberto Ruiz Aguilar")
    case "2":
        print("La directora del área de Terapia Física es la Med.Rosalía Huerta Robles")
    case "3":
        print("El director del área de Mecatrónica es el Ing.Luis Alberto Ruiz Aguilar")
    case "4":
        print("El director del área de Innovación de Negocios y Mercadotecnia es el Mtro.Zerefino Martell Labra")
    case "5":
        print("El director del área de Manejo Sustentable de Recursos Naturales es el Mtro.Edwin Alberto San Román Arteaga")        
    case "6":
        print("El director del área de Metal Mecánica es el Ing.Cesar Hidalgo")
    case "7":
        print("El director del área de Mantenimiento Industrial es el Mtro.Edwin Alberto San Román Arteaga")
    case "8":
        print("El director del área de Industrial es el Ing.Cesar Hidalgo")
    case "9":
        print("El director del área de Contabilidad es el Mtro.Zerefino Martell Labra")
    case "10":
        print("El director del área de Gestión de Capital Humano es el Mtro.Zerefino Martell Labra")
    case "11":
        print("El director del área de Diseño Textil y Moda es el Ing.Cesar Hidalgo")
    case "12":  
        print("La directora del área de Enfermería es la Med.Rosalía Huerta Robles")
    case "13":
        print("La directora del área de Cirujano Medico y Partero es la Med.Rosalía Huerta Robles")
    case "14":
        print("El director del área de Ingeniería Civil es el Ing.Cesar Hidalgo")