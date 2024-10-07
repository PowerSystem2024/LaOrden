
# Ejercicio 4: calculadora de impuetsos

# crear una funcion para calcular el total de un pago inclutendo un impuesto aplicado (IVA)
# Formula: pago:total  pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
# Proporcione el pago sin impuesto: 1000
# Proporcione el monto del impuesto: 21
# Pago con impuesto: xxxxx


def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

pago_sin_impuesto(float(input('Digite el monto del impuesto a aplicar: ')))
pago_con_impuesto = calcular_total_pago(pago_con_impuesto, impuesto)
print(f"El pago con impuesto es: {pago_con_impuesto}")