nUsuario = input("Ingrese su nombre de usuario:\n -> ")

edadCliente = int(input(f"Hola {nUsuario}, ingrese la edad del cliente:\n -> "))

if edadCliente < 4:
    print("¡El cliente puede entrar gratis!")
elif edadCliente >= 4 and edadCliente <= 18:
    print("El cliente debe pagar $5")
else:
    print("El cliente debe pagar $10")