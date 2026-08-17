# ================= SISTEMA DE VENTAS (con funciones) =================

inventario = {
    "arroz":  {"precio": 15.5, "cantidad": 40},
    "frijol": {"precio": 12.0, "cantidad": 25},
    "aceite": {"precio": 35.0, "cantidad": 10},
    "azucar": {"precio": 18.0, "cantidad": 30},
    "sal":    {"precio": 5.5,  "cantidad": 0},
    "leche":  {"precio": 32.0, "cantidad": 20}
}

ventas = []       


def mostrar_menu():
    print("\n=== SISTEMA DE VENTAS ===")
    print("1. Ver inventario")
    print("2. Hacer una venta")
    print("3. Ver ventas totales")
    print("4. Reponer stock")
    print("5. Crear producto")
    print("6. salir")


def ver_inventario():
    for producto in inventario:
        precio = inventario[producto]["precio"]
        cantidad = inventario[producto]["cantidad"]
        estado = "AGOTADO" if cantidad == 0 else f"{cantidad} unidades"
        print(f"- {producto}: ${precio:.2f} | {estado}")


def precio_con_iva(precio):
    return round(precio * 1.19, 1)


def costo_compra(productos, inventario):
    total = 0
    for producto in productos:
        total += inventario[producto]["precio"] * productos[producto]["cantidad"]
    return round(precio_con_iva(total) * 1000)


def hacer_compra(inventario):
    compra = {}
    print("\n--- NUEVA COMPRA ---")
    print("Productos disponibles:", " ".join(inventario.keys()))
    print("Escribe 'fin' para terminar.")

    while True:
        producto = input("Producto: ").lower()

        if producto == "fin":
            break

        if producto not in inventario:
            print("Este producto no esta disponible")
            continue

        if inventario[producto]["cantidad"] == 0:
            print("Este producto esta agotado")
            continue

        cantidad = int(input(f"Cuantas unidades de {producto}? "))


        if cantidad > inventario[producto]["cantidad"]:
            print(f"Limite excedido, hay {inventario[producto]['cantidad']} unidades")
            continue

        inventario[producto]["cantidad"] -= cantidad

        compra[producto] = {"cantidad": cantidad}
        print(f"Agregado: {producto} x {cantidad}")

    return compra


def mostrar_ticket(compra, inventario):
    if not compra:
        return
    print("\n--- TICKET ---")
    for producto in compra:
        precio = inventario[producto]["precio"]
        cantidad = compra[producto]["cantidad"]
        print(f"{producto.upper()}: ${precio * cantidad:,.2f} x {cantidad}")
    print("-" * 20)
    print(f"TOTAL: ${costo_compra(compra, inventario):,.0f}")

def ventas_totales():
    if not ventas:
        print("Todavia no hay ventas")
    else:
        for i, venta in enumerate(ventas, 1):
            total = costo_compra(venta, inventario)
            print(f"Venta {i}: ${total:,.0f}")

def crear_producto(inventario):
    while True:
        print("\n--- CREAR PRODUCTO ---")
        print("Escribe 'fin' para terminar.")
        producto=input("Que producto nuevo quieres agregar: ")
        if producto == "fin":
                    break
        if producto in inventario:
            print("Este producto ya existe")
            continue
        while True:                    
            precio = input("Ingresa el valor del producto: ")
            try:
                precio = float(precio)
                break                  
            except ValueError:
                print("Porfavor ingrese un precio correcto")
            

        while True:                    
            cantidad = input("Porfavor ingresa las unidades disponibles: ")
            try:
                cantidad = int(cantidad)
                break
            except ValueError:
                print("Porfavor ingrese una cantidad correcta")
        inventario[producto] = {"precio": float(precio), "cantidad": int(cantidad)}
        print(f"Se ha agregado {producto} al inventario con precio ${precio} y cantidad {cantidad}.")
        


def reponer_inventario(inventario):
    while True:
        print("\n--- REPONER INVENTARIO ---")
        print("Que producto quieres reponer:",", ".join(inventario.keys()))
        print("Escribe 'fin' para terminar.")
        producto=input("Producto:")
        if producto == "fin":
            break
        if producto in inventario:
            cantidad=int(input("Cuanta cantidad deseas añadir:"))
            inventario[producto]["cantidad"] += cantidad
            print(f"Se han añadido {cantidad} unidades de {producto}. Total: {inventario[producto]['cantidad']} unidades.")
        else:
            print("Este producto no esta en la lista")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            ver_inventario()
        elif opcion == "2":
            compra = hacer_compra(inventario)
            mostrar_ticket(compra, inventario)
            ventas.append(compra)
        elif opcion == "3":
            ventas_totales()
        elif opcion == "4":
            reponer_inventario(inventario)
        elif opcion == "5":
            crear_producto(inventario)
        elif opcion == "6":
            print("Hasta luego!")
            break
        else:
            print("Opcion no valida")


main()
