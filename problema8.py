#time = input("hora")

horaIngresada = input("Ingrese una hora: ")
hours, minutes = horaIngresada.split(":")

#int(hours)
#int(minutes)
#float(horaIngresada)
if hours == "7" and minutes == "0" :
    print(f"La hora ingresada {horaIngresada} corresponde al desayuno")
    
print("hora de almuerzo")