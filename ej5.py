#ej5

importe_sin_iva = float(input("Escribe importe (€):"))
tipo_iva = float(input("Escribe tipo de iva (%):"))
importe_final = importe_sin_iva * (1 + tipo_iva / 100)
print(f"El precio final es: {importe_final:.2f} €")
