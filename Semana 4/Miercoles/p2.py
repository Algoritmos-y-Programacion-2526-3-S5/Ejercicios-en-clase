def calcular_impuesto(precio, categoria):
    if categoria == "tecnologia":
        return precio * 0.16
    elif categoria == "hogar":
        return precio * 0.08
    else:
        return 0

def aplicar_descuento(precio, cupon):
    if cupon == "TECH10" and precio > 500:
        return precio * 0.9
    elif cupon == "HOGAR20":
        return precio * 0.8
    else:
        return precio

def procesar_compra(carro_de_compra, cupon):
    total_final = 0
    for item in carro_de_compra:
        impuesto = calcular_impuesto(item.get("precio"), item.get("categoria"))
        total_con_descuento = aplicar_descuento(item.get("precio"), cupon)
        total = total_con_descuento + impuesto
        total_final += total
        print(item.get("producto"), total, sep=" - " )
    print("El total final fue: ", total_final)
        
def main():
    print("***** WELCOME TO TechNova ******")
    carrito = [
        {"producto": "MacBook Pro M3", "precio": 2500, "categoria": "tecnologia"},
        {"producto": "Cafetera Express", "precio": 120, "categoria": "hogar"},
        {"producto": "Monitor 4K", "precio": 450, "categoria": "tecnologia"},
        {"producto": "Set de Cuchillos", "precio": 80, "categoria": "hogar"}
    ]
    cupon = "TECH10"
    procesar_compra(carrito, cupon)
    
    
main()