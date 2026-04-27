volumen_lluvia = float(input("valor:"))
reservorio = float(input("reservorio:"))
volumen_lluvia = volumen_lluvia * 0.9
volumen_lluvia += reservorio
reservorio *= 1.05
