# Tienes una lista con los precios de 5 productos
precios = [12.5, 8.9, 3.4, 21.0, 7.75]

# 1) Calcula el total usando sum()
total = sum(precios)
print("Total:", total)

# 2) Calcula el precio promedio (total / número de productos)
#    Pista: usa len(precios)
promedio  = total/len(precios)
print("Promedio:", round(promedio, 2))
print("El precio maximo es de:",max(precios))
print("El precio maximo es de:",min(precios))


# 3) Muestra el producto más caro y el más barato
#    Pista: usa max() y min()