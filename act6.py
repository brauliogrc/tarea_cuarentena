palabra=str(input("Ingrese una palabra: "))
try:
    archivo1=open("Tarea_3_cuarentena/palabra_act6.txt", "w")
    """como primer parametro pasamos la ruta o direccion junto con el nombre del archivo, como segundo parametro pasamos si se abrira
    el archivo como solo lectura o como escritura, 'w' crea el archivo y nos permite escribir en el"""
    '''si cambiamos "w" por "r", entonces nuestra instruccion abre un archivo en forma de lectura'''
    archivo1.write(palabra)
    archivo1.close()
    print("Archivo creado")
except:
    print("Error en la cracion del archivo")