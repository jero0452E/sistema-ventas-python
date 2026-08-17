prices = {"pan": 2500, "leche": 3200, "huevos": 4000, "cafe": 1500}
total=0
maximo_producto=("pan", 2500)
for elements, price in prices.items():
    total += price
    print(f"El {elements} cuesta: ${price}")
    if maximo_producto[1] < price:
        maximo_producto=(elements, price)

print(f"El valor de todos lo productos es de: ${total}")
print(f"El producto con el valor mas alto es {maximo_producto[0]} con un precio de ${maximo_producto[1]}")
print(type(maximo_producto))