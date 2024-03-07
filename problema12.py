
#print(len(nombreArchivo))
#print(nombreArchivo[-3])
lista = ["gif","jpg","jpeg","png","pdf","txt","zip"]
nombreArchivo = input("Ingrese el nombre del archivo: \n -> ")
#print(nombreArchivo.lower())
separarExtension = nombreArchivo.split(".")


if separarExtension[-1] in lista:
    #separarExtension.lower()
    print(separarExtension[-1])
    nombreArchivoNuevo = nombreArchivo.replace(".","/")
    print(nombreArchivoNuevo)
else:
    print(separarExtension[0]+"/octet-stream")

