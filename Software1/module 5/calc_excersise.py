menu_list = "select option\n1. add \n2. subtract \n3. multiply \n0. exit\n"
selection = input(menu_list)

while selection != "0":
    first_number = float(input("first number: "))
    second_number = float(input("second number: "))

    if selection == "1":
        print(f"result: {first_number + second_number:}")
    elif selection == "2":
        print(f"result: {first_number - second_number:}")
    elif selection == "3":
        print(f"result: {first_number * second_number:}")
    else:
        print(f"Inorrect option")

    menu_list = "select option\n1. add \n2. subtract \n3. multiply \n0. exit\n"
    selection = input(menu_list)

    ### yes this is a copy
    ### 