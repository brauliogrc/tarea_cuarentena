cadena=str(input("Ingrese una palabra: "))
lista=list(cadena)
lista.pop(0)
cadena_def="".join(lista)
'''el metodo ".join()" concatena cualquier numero de
cadenas, este caso concatena a la variable"cadena_def" todos los 
elementos de nuestra lista'''
print(cadena_def)