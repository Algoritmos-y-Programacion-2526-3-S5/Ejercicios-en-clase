lista = [1,2,3,1,1,3]
cont = 0
lista_pares = []
for i in range(len(lista)): #(0,5)
    for j in range(i+1, len(lista)):
        print(i,j, sep=",")
        if lista[i] == lista[j]:
            lista_pares.append((i,j))
            cont += 1 
            
print(lista_pares)
print(cont)

# (0,3) (0,4) (2,5) (3,4)