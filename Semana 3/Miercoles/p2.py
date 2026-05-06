lista = []

for number in range(11):
    if number > 0:
        lista.append(number)
    
lista.reverse()

for elemento_de_la_lista in lista:
    print(elemento_de_la_lista, end=",")
        