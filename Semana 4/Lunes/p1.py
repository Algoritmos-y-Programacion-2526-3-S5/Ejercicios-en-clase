currencies = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

currency = input("Please enter a currency: \n1-Euro\n2-Dollar\n3-Yen\n->")

currency_dict = {"1":"Euro", "2":"Dollar", "3":"Yen"}

if currency_dict[currency] in currencies:
    print(currencies[currency_dict[currency]])
else:
    print("No esta la currency")