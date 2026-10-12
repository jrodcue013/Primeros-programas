#ej15.py

cantidad = float(input("Introduce la cantidad depositada: "))
interes = 0.04
for i in range(1, 4):
    cantidad *= (1 + interes)
    print(f"Ahorros tras el año {i}: {cantidad:.2f} €")
