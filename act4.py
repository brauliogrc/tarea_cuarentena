def cantidad_consonantes(cadena):
    vocales=['a','A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    resultado=''
    for letra in cadena:
        if letra not in vocales:
            resultado+=letra
    total=len(resultado)
    print(total)

while (1>0):
    cadena=input("Ingrese cadena: ")
    cantidad_consonantes(cadena)