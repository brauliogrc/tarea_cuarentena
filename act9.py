lista=[]
i=0
while(i<10):
    numero=int(input("Ingrese numero " + str(i+1) + ": "))
    lista.append(numero)
    i+=1

for i in range(len(lista)-1, 0, -1):
    for j in range(i):
        if (lista[j] > lista[j+1]):
            aux = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = aux

#lista.sort()
print(lista)
print(max(lista))
