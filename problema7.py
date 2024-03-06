print("*** ¿Qué operación desea realizar? ***\n")

print("1. Mostrar una suma de los dos números")
print("2. Mostrar una resta de los dos números(el primero menos el segundo)")
print("3. Mostrar una multiplicación de los dos números")
print("NOTA: En caso de introducir una opción inválida, el programa informará de que no es correcta. \n")

eleccion = int(input("Escoga una opción válida: \n ->"))


##while True:


if eleccion == 1:
    op1n1 = int(input("\nEscriba el primer número:\n -> "))
    op1n2 = int(input("Escriba el segundo número:\n -> "))
    resultado = op1n1 + op1n2
    print(f"El resultado es: {resultado}")

elif eleccion == 2:
    op2n1 = int(input("Escribe el primer número:\n -> "))
    op2n2 = int(input("Escribe el segundo número:\n -> "))
    resultado = op2n1 - op2n2
    print(f"El resultado es: {resultado}")
elif eleccion == 3:
    op3n1 = int(input("Escribe el primer número:\n -> "))
    op3n2 = int(input("Escribe el segundo número:\n -> "))
    resultado = op3n1 * op3n2
    print(f"El resultado es: {resultado}")
else:
    print("Opción inválida, intente de nuevo.")








