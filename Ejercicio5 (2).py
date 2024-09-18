def verificacion(valor):
    if valor.strip()=="":
        valor=None
        
    if valor is None:
        text="No ha ingresado un valor (esta vacio)"
    else:
        text=f"El valor es: {valor}"

    return text

valor=input("Ingrese algo: ")

print(verificacion(valor))