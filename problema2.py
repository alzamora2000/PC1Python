nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")

costoPlato = float(input("¿Cuál fue el costo total de su comida?\n $"))

propina = float(input("Indique el porcentaje de propina que le dejará al mesero: \n %"))

propinaFinal = costoPlato * propina/100

print(f"La propina que se le dejará al mesero es de: \n ${propinaFinal}")

