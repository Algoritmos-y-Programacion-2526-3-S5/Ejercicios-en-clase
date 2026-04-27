precio_hamburguesa = 12
precio_papas = 5
costo_envio = 3
descuento = 4

cantidad_hamburguesas = int(input("Por favor ingresa la cantidad de hamburguesas:"))
cantidad_papas = int(input("Por favor ingresa la cantidad de papas:"))

costo_total_hamburguesas = precio_hamburguesa * cantidad_hamburguesas
costo_total_pedido = costo_total_hamburguesas + (precio_papas * cantidad_papas)
costo_final = costo_total_pedido - descuento

print("El costo total de las hamburguesas es:",costo_total_hamburguesas)
print("El costo total del pedido es:",costo_total_pedido)
print("El total a pagar es:",costo_final)