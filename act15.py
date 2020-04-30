cantn=int(input("ingrese la cantidad de numeros: "))
lista=[]
primos=[]
i=0

while(i<cantn):
    numero=int(input("Ingrese numero " + str(i) + ": "))
    lista.append(numero)
    i+=1

i=0
cantidad=len(lista)
while(i<cantidad):
    comparar=lista[i]
    for j in (2, comparar):
        if (not(comparar%j==0)):
            primos.append(comparar)
    i+=1
    if(comparar==1):
        primos.append(comparar)
    if(comparar==2):
        primos.append(comparar)

print(primos)