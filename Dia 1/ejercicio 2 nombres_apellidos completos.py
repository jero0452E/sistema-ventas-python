nombres = ["Ana", "Luis", "Maria", "Pedro"]
apellidos = ["Garcia", "Lopez", "Perez", "Sanchez"]

# Combina cada nombre con su apellido usando zip()
# La variable "completos" debe ser una lista de tuplas
completos = tuple(zip(nombres, apellidos))
print(completos)

# Después, convierte la primera tupla en un string
# Ejemplo: "Ana Garcia"
primer_nombre = completos[0]
print(primer_nombre)