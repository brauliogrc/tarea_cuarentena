cadena=str(input("Ingrese una palabra: "))
lista=list(cadena)
lista.pop(0)#borra lo que se encuente en la posicion definida, en este caso la posicion 0
lista.pop()#borra lo que se ecncuentra almacenado en la ultima posicion de nuesra lista
cadena_def="".join(lista)
'''el metodo ".join()" concatena cualquier numero de
cadenas, este caso concatena a la variable"cadena_def" todos los 
elementos de nuestra lista'''
print(cadena_def)