print("Dados los datos P y Q, determine so los mismos satifacen la siguiente operción: P^3 Q^4-2*P < 680, de ser verdad imprimir P y Q")

p = float(input("Ingresa el valor de P:  "))

q = float(input("Ingresa el valor de Q:  "))

if (p**3 * q**4) - (2 * p) < 680: 
    
    print("P:  ",p,"Q:  ",q)