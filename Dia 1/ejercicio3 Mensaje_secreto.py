mensaje = "PYTHON-ES-GENIAL-APRENDE"

# 1) Separa el mensaje en palabras usando split("-")
palabras = mensaje.split("-")
print(palabras)
print(f"Hay {len(palabras)} palabras en el texto")
print("la primera palabra es", palabras[0])
print("la segunda palabra es", palabras [-1])
mensaje_new=" ".join(palabras)
print(mensaje_new)


# 2) Cuenta cuántas palabras hay (len)
# 3) Muestra la primera y la última palabra (índices 0 y -1)
# 4) Junta las palabras de nuevo con un espacio usando " ".join(palabras)