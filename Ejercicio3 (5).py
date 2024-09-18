#Entrada
texto=input("Ingrese el texto: ")

#Proceso
mayus=texto.upper()
cant=len(texto)

if "python" in texto:
    valor="SI"
else:
    valor="NO"

#Salida
print(f"\nEl texto en mayúscula es: {mayus} \n\nEl texto tiene {cant} carácteres \n\nEl texto {valor} contiene la palabra python")

