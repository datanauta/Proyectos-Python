
def calcular_precio_descuento(precio,descuento):

    precio_descuento = precio - (precio*descuento /100)

    return precio_descuento

precio = float(input('Ingresa el precio del producto:'))
descuento = float(input('Ingresa el porcentaje del descuento:'))

precio_final = calcular_precio_descuento(precio,descuento)
print(f'El precio final con descuento del producto es: {precio_final:.2f}')

