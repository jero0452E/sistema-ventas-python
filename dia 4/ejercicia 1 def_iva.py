def precio_con_iva(precio):
    precio_final = precio * 1.19
    return round(precio_final, 1)

print(precio_con_iva(100))   # debe dar 119.0
print(precio_con_iva(50))    # debe dar 59.5

def ganancia(precio, costo):
    # usa precio_con_iva dentro
    return precio_con_iva(precio)-costo
    ...

print(ganancia(100, 60))   # debe dar 59.0