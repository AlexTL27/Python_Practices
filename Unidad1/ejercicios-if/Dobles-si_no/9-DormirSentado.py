#####Hecho por Alex Efrén Téllez Limón#####

print("Una persona enferma, que pesa 70 kg., se encuentra en reposo y desea saber cuántas calorías consume su cuerpo durante todo el tiempo que realice una misma actividad. Las actividades que tiene permitido realizar son únicamente dormir o estar sentado en reposo. Los datos que tiene son que estando dormido consume 1.08 calorías por minuto y estando sentado en reposo consume 1.66 calorías por minuto.")


opc = int(input("Indica que actividad realizaste: 1.-Dormir, 2.-Estar sentado:  "))

if opc == 1:
    time = int(input("Indica el tiempo que realizaste: "))
    print(time * 1.08)
elif opc == 2:
     time = int(input("Indica el tiempo que realizaste: "))
     print(time * 1.66)