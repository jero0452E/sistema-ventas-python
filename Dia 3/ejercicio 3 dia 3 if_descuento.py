import time
from turtle import delay


age = 5
price_normal = 100

# Completa con if / elif / else
if age < 5:
    print("Entry free")
elif age <= 17 :
    price_young = price_normal*0.50
    print(f"You have to pay: ${price_young:.0f}")
elif  age <= 59:
    print(f"You have to pay: ${price_normal}")
else:
    price_old = 25
    print(f"You have to pay: ${price_old}")

