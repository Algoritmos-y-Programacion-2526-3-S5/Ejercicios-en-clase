saldo_inicial = 0.0
deposito = 0.1

# Simulamos 3 depósitos
saldo_actual = deposito + deposito + deposito
saldo_actual = round(saldo_actual,1)

print(f"Saldo calculado: {saldo_actual}")

if saldo_actual == 0.3:
    print("Confirmado: Saldo Correcto.")
else:
    # Este bloque se ejecuta aunque parece que el saldo es 0.3
    print("Error Crítico: El saldo no coincide con 0.3")