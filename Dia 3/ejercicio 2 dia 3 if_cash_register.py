precio_articulo = 35.0
cantidad = 3
pago = 100

total = precio_articulo * cantidad

# 1) Si el total es mayor a 80, aplica 15% de descuento
#    y muéstralo: "Descuento aplicado: $X"
#    (el total debe cambiar con el descuento)
if total > 80:
    descuento = total * 0.15
    total= total - descuento
    print(f"Descuento aplicado: ${descuento:.2f}")

# 2) Si el pago es mayor o igual al total, muestra "Su cambio es: $Y"
#    si no, muestra "Le faltan $Z"
if pago >= total:
    print(f"Su cambio es de: ${pago-total}")
else:
    print(f"le faltan ${total-pago}")