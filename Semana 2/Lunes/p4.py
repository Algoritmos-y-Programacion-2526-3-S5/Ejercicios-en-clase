number = int(input("Numerador:"))
number2 = int(input("Denominador:"))

if number2 == 0:
    print("Error, el denominador no puede ser cero")
else: 
    print(f"Resultado = {number/number2}")