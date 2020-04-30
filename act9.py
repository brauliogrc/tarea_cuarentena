lista=[]
i=0
while(i<10):
    numero=int(input("Ingrese numero " + str(i+1) + ": "))
    lista.append(numero)
    i+=1
lista.sort()
print(lista)
print(max(lista))

