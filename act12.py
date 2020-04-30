dias=int(input("Ingrese la cantidad de dias: "))
horas=int(input("Ingrese la cantidad de horas: "))
tarifa=float(input("Ingrese la tarifa por hora: "))
total_dias=(tarifa*8)*dias
total_horas=tarifa*horas
dinero_total=total_dias+total_horas
print("Total de dinero ganado: " + str(dinero_total))