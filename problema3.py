print ("*** JUGUETERÍA ***")

payaso = 112
muneca = 75

cantPayasos = int(input("Indique el n° de payasos que hay en el paquete: \n ->"))

cantMunecas = int(input("Indique el n° de muñecas que hay en el paquete: \n ->"))

payasosFinal = payaso * cantPayasos
munecasFinal = muneca * cantMunecas
pesoPaquete = payasosFinal + munecasFinal
pesoKg = pesoPaquete/1000

print("\n *** RESUMEN DEL PEDIDO ***")
print(f"PAYASOS: {cantPayasos}")
print(f"PESO: {payasosFinal}g.")
print("----------------------------")
print(f"MUÑECAS: {cantMunecas}")
print(f"PESO: {munecasFinal}g.")
print("----------------------------")
print(f"PESO TOTAL DEL PAQUETE: {pesoPaquete}g.|{pesoKg}kg.")