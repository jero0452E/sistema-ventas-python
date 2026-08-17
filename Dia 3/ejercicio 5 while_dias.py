ahorro = 0
dias = 0
meta = 7000

# Usa un while:
#   mientras el ahorro sea menor a la meta:
#   suma 500, cuenta el día, y muestra "Día X: $ahorro"
# Al final muestra "Conseguido en X días"
while ahorro < meta:
    dias += 1
    ahorro += 500
    print(f"Dia {dias} ahorrado: ${ahorro}")
else:
    print(f"Conseguido en {dias} dias.")


