print(" ********** Bienvenidos a la Pizzeria Bella Napol ********** ")

pizza_type = int(input("Por favor ingresa el tipo de pizza\n1-Vegetariana\n2-No Vegetariana\n->"))

if pizza_type == 1:
    ingredient = input("Por favor ingresa el ingrediente a agregar en la pizza\n1-Pimiento\n2-Tofu\n->")
    if ingredient == "1":
        ingredient = "Pimiento"
    else:
        ingredient = "Tofu"
    print(f"La pizza seleccionada es Vegatariana y tiene Tomate, Mozzarella y {ingredient}")
elif pizza_type == 2:
    ingredient = input("Por favor ingresa el ingrediente a agregar en la pizza\n1-Peperoni\n2-Jamon\n3-Salmon\n->")
    if ingredient == "1":
        ingredient = "Peperoni"
    elif ingredient == "2":
        ingredient = "Jamon"
    else:
        ingredient = "Salmon"
    print(f"La pizza seleccionada es No Vegatariana y tiene Tomate, Mozzarella y {ingredient}")
else: 
    print("Opcion de Pizza invalida")