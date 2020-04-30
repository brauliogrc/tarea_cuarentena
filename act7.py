nom_archivo=str(input("Ingrese el nombre del archivo, sin espacios ni caracteres especiales: "))
palabra=str(input("Ingrese palabra: "))
try:
    archivo=open("Tarea_3_cuarentena/"+nom_archivo+".txt", "w")
    archivo.write(palabra)
    archivo.close()
    print("Archivo creado")
except:
    print("Error en la cracion del archivo")