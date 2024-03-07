lista = [1, 1, 2, 3, 4, 4, 5, 1]
listaProcesada = []

for i in lista:
    if i not in listaProcesada:
        listaProcesada.append(i)

print(f"Lista inicial: {lista}")
print(f"Lista procesada: {listaProcesada}")