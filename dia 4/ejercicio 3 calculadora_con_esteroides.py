inventario = {
    "arroz":  {"precio": 15.5, "cantidad": 40},
    "leche":  {"precio": 32.0, "cantidad": 20},
    "cafe":   {"precio": 28.0, "cantidad": 15}
}
compra = {
    "arroz":  {"cantidad": 2},
    "leche":  {"cantidad": 1},
    "cafe":   {"cantidad": 3}
}


def precio_con_iva(precio):
    return round(precio * 1.19, 1)

def descuento(precio, porcentaje):
    return round(precio * (1 - porcentaje / 100), 1)

def costo_total(productos, inventario):
    total = 0
    for producto in productos:            # recorre la LISTA de compra
        precio = inventario[producto]["precio"]   # busca ese producto en el inventario
        cantidad = productos[producto]["cantidad"]
        total += precio * cantidad    # suma con IVA
    return round(precio_con_iva(total) * 1000 )




print(f"Costo total: ${costo_total(compra, inventario):,.0f}")
    # productos = lista de nombres ej: ["arroz", "leche"]
    # inventario = diccionario {producto: {"precio": ..., "cantidad": ...}}
    # 1) recorre con un for
    # 2) busca el precio de cada producto en el inventario
    # 3) acumula el total con IVA (usa precio_con_iva)
    # 4) devuelve el total