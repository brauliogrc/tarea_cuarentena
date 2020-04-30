def anti_vocal(cadena):
    vocales=['a','A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    resultado=''
    for letra in cadena:
        if letra not in vocales:
            resultado+=letra
    print(resultado)

while (1>0):
    cadena=input("Ingrese cadena: ")
    anti_vocal(cadena)
