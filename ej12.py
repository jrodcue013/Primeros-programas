#ej12.py

peso = float(input("Introduce tu peso (kg): "))
altura = float(input("Introduce tu estatura (m): "))
imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal es {imc:.2f}")
