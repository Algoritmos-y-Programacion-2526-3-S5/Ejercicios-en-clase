#ej 1|
numero = input("Ingrese un numero:")

if numero.isnumeric():
    numero = int(numero)
    print(numero)
else: 
    print("numero errado")

#ej 2
palabra = input("Ingrese una palabra:")

print(palabra.title())