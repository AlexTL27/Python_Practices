print("Universidad Tecnológica de la Sierra Hidalguense Carreras: \
\n1.- Tecnologías de la Información y Comunicación área Sistemas Informáticos.\
\n2.- Tecnologías de la Información y Comunicación área Redes y Telecomunicaciones.\
\n3.- Mecánica.\
\n4.- Terapia Física")

print("Selecciona la carrera:  ")
op = input()

match op:
 case "1":
  print("La directora del área de Tecnologías de la Información y Comunicación área \nSistemas Informáticos es la Dra. Luz Angelina Albores Villatoro.")
 case "2":
  print("El director del área de tecnologías de la información y comunicación área \nsistemas informáticos es el sr. Gustavo Ordaz")
 case "3":
  print("El director del área de mecánica es el sr. Carlos Diaz")
 case "4":
  print("La directora del área de Terapia Física es la Dra. Susana Villa")
 case _:
  print("Opción no válida")
       
    
