# ============ PARTE 1: Tu inventario ============
# Un diccionario donde cada producto tiene su precio y cantidad
inventario = {
    "arroz":   {"precio": 15.5, "cantidad": 40},
    "frijol":  {"precio": 12.0, "cantidad": 25},
    "aceite":  {"precio": 35.0, "cantidad": 10},
    "azucar":  {"precio": 18.0, "cantidad": 30},
    "sal":     {"precio": 5.5,  "cantidad": 0}
}

# 1) Muestra el precio del arroz (clave "arroz", dentro "precio")
#    Pista: inventario["arroz"]["precio"]
print(inventario["arroz"]["precio"])

# 2) Imprime TODOS los productos (solo los nombres)
#    Pista: recorre con for... in inventario (te da las claves)
print(" ".join(inventario.keys()))

# 3) Calcula el valor total del inventario:
#    para cada producto: precio * cantidad, y súmalo todo
#    Pista: lleva una variable total = 0 e ir sumando
value_total = inventario["arroz"]["precio"]*inventario["arroz"]["cantidad"]+inventario["frijol"]["precio"]*inventario["frijol"]["cantidad"]+inventario["aceite"]["precio"]*inventario["aceite"]["cantidad"]+inventario["azucar"]["precio"]*inventario["azucar"]["cantidad"]+inventario["sal"]["precio"]*inventario["sal"]["cantidad"]
print(f"el valor total es de:{value_total}")

# ============ PARTE 2: El pedido ============
# El cliente pide 5 productos. Guárdalos en una TUPLA (no cambiarán):
pedido = ("arroz", "aceite", "arroz", "sal", "frijol")

# 4) ¿Cuántos artículos pidió en total? (len)
print(f"el cliente pidio {len(pedido)} articulos en total.")
# 5) ¿Cuántos productos DIFERENTES pidió? (set + len)
print(f"El clinete pidio {len(set(pedido))} articulos diferentes")
# 6) Muestra el producto con nombre más largo
#    Pista: pedido[0], pedido[1]... o recorre comparando con len()
print(f"el producto con nombre mas largo es {max(pedido, key=len)}")
print(f"Los productos con los nombres mas largo son {pedido[1]} y tambien {pedido[-1]}")

# ============ PARTE 3: El ticket ============
# 7) Arma el ticket así:
#    "ARROZ: $15.5 x 2 = $31.0"
#    Hazlo para los 5 artículos del pedido (uno por línea)
#    Pista: usa f-strings como ya aprendiste
total = 0                      # empieza en cero
for p in pedido:
    precio = inventario[p]["precio"]
    cantidad = inventario[p]["cantidad"]
    print(f"{p.upper()}: ${precio} x {cantidad} = ${precio * cantidad}")
    total = total + precio * cantidad    # ← esta línea va DENTRO del for

# 8) Suma el total del ticket y muéstralo

print(f"TOTAL: ${total}")
