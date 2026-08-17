codigos = ["abc", "user", "admin123", "clave", "test"]

for codigo in codigos:
    if codigo == "admin123":
        print("Acceso concedido")
        break
    print(f"Intento fallido: {codigo}")
else:                          
    print("Acceso denegado: no se encontró el código")
# Usa un for para revisar cada código:
#   si es "admin123", imprime "Acceso concedido" y detén el bucle con break
#   si no, imprime "Intento fallido: abc"