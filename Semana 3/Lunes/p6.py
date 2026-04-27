number = int(input("Please enter a number:"))
aux = 2
is_prime = True

while aux < number:
    if number % aux == 0:
        is_prime = False
        break
    aux += 1

if is_prime and number > 1:
    print("Es primo")
else:
    print("No es primo")

