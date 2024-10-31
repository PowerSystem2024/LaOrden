
# Ejercicio 4: calculadora de impuetsos

# crear una funcion para calcular el total de un pago inclutendo un impuesto aplicado (IVA)
# Formula: pago:total  pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
# Proporcione el pago sin impuesto: 1000
# Proporcione el monto del impuesto: 21
# Pago con impuesto: xxxxx

def calculadoraImpositiva(importeNeto,impuesto):
    precioFinal=importeNeto+(impuesto*importeNeto/100)
    print(f"Importe sin impuestos: ${importeNeto}")
    print(f"IVA {impuesto}%: ${impuesto*importeNeto/100}")
    print(f"Precio final: ${precioFinal}")

importeNeto=int(input("Ingrese el monto del importe neto de compra: $ "))
impuesto=int(input("Ingrese el porcentaje del IVA: "))

calculadoraImpositiva(importeNeto,impuesto)