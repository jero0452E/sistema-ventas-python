nota = 7.5

# 1) Si la nota es mayor o igual a 6, imprime "APROBADO"
#    si no, imprime "REPROBADO"
if nota >= 6:
    print("approved")
else:
    print("failed")

# 2) Si la nota es mayor o igual a 9, además imprime "Excelente"
#    (solo para los de nota alta)
if nota >= 9:
    print("excellent")

# 3) Si la nota es exactamente 5.5, imprime "Tienes que repetir"
#    (caso especial)
if nota == 5.5 :
    print("You have to repeat")