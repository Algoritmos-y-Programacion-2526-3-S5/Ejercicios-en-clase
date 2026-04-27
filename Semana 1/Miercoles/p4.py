total_money = float(input("Por favor ingresa el monto a invertir:"))
interest = float(input("Por favor ingresa el interes:"))

year_1 = total_money + (total_money * interest/100)
year_2 = year_1 + (year_1 * interest/100)
year_3 = year_2 + (year_2 * interest/100)

print(f"El capital obtenido de la inversion es: {year_3}, con un interes del {interest}%")