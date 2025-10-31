print("menú en el que muestre por lo menos 5 géneros musicales que te agraden, el usuario debe poder elegir uno de ellos y este debe mostrar como mínimo 3 intérpretes de ese género musical.")

print("1.-rap, 2,-pop, 3,-rock, 4.-sierreño, 5,-bolero")
op = input()

match op:
 case "1":
  print("Will Smith, Eminem, Misses")
 case "2":
  print("Rihanna, Ariana Grande, Dua Lipa")
 case "3":
  print("Freddie, Kurt, Axl")
 case "4":
  print("Perdidos, Carin, MP")
 case "5":
  print("Luis Miguel, Julio Jaramillo, Orlando")
 case _:
  print("Opción no válida")
       
    

