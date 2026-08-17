# ================= SISTEMA DE VENTAS (sin funciones) =================

inventario = {
    "arroz":  {"precio": 15.5, "cantidad": 40},
    "frijol": {"precio": 12.0, "cantidad": 25},
    "aceite": {"precio": 35.0, "cantidad": 10},
    "azucar": {"precio": 18.0, "cantidad": 30},
    "sal":    {"precio": 5.5,  "cantidad": 0}
}

opcion = ""

while opcion != "3":
    print("\n=== SISTEMA DE VENTAS ===")
    print("1. Ver inventario")
    print("2. Hacer una venta")
    print("3. Salir")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        for producto in inventario:
            precio = inventario[producto]["precio"]
            cantidad = inventario[producto]["cantidad"]
            estado = "AGOTADO" if cantidad == 0 else f"{cantidad} unidades"
            print(f"- {producto}: ${precio:.2f} | {estado}")
    elif opcion == "2":
        print("Todavia no implementado")
    elif opcion == "3":
        print("Hasta luego!")
    else:
        print("Opcion no valida")
