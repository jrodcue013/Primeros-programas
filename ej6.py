#ej6.py

importe_final = float(input("importe final de un artículo(€):"))
importe_sin_iva = importe_final * 10 / 100
iva_pagado = importe_final - importe_sin_iva
print(f"Importe sin IVA: {importe_sin_iva:.2f} €")
print(f"IVA pagado: {iva_pagado:.2f} €")
