def precio_con_iva(precio):
    return round(precio * 1.19, 1)

def descuento(precio, porcentaje):
    return round((precio * porcentaje / 100), 1)
print(descuento(300, 20))
    # devuelve el precio menos el porcentaje indicado
    # ej: descuento(100, 10) → 90.0

def precio_final(precio, porcentaje_desc):
    # aplica el descuento y LUEGO el IVA
    # usa las dos funciones de arriba
    """ ej: precio_final(100, 10) → 107.7 """
    return precio_con_iva(descuento(precio, porcentaje_desc))
   
print(precio_final(100, 10))