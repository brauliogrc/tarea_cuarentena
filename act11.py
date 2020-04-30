from numero_a_letras import numero_a_letras 
'''importacion del scrip y funcion
que convierte los umeros a letras'''
cant_num=int(input("Ingrese la cantidad de numeros: "))
i=0
lista=[]
while(i<cant_num):
    num_flotante=float(input("Ingrese numeros entre el 1.0 y el 10.0: "))
    if ((num_flotante<1.0) and (num_flotante>10.0)):
        print("El numero debe estar entre 1.0 y 10.0")
    else:
        lista.append(num_flotante)
        i+=1
lista.sort()#ordena de forma acendente todos nuestros elementos de la lista
mayor=max(lista)
entero=int(mayor)
print(lista)
print(entero)
print(numero_a_letras(entero))