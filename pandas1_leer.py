import pandas as pd

ventas = pd.read_csv("ventas.csv")
print(ventas)
print(ventas["producto"])        # 1) la columna producto
print(ventas[["producto", "cantidad"]])   # 2) dos columnas juntas
print(ventas[ventas["producto"] == "arroz"])   # 3) solo las filas de arroz
print(ventas["precio"].sum())    # 4) la suma de la columna precio
print(ventas["cantidad"].mean()) # 5) promedio de cantidad