number = int(input("Please enter a number:"))
aux = 1
suma = 0
print("Los divisores son:")
while aux < number:
    if number % aux == 0:
        suma += aux
        print(aux)
    aux += 1
    
    
if suma == number:
    print(f"El numero {number} es perfecto")
else:
    print(f"El numero {number} no es perfecto")
