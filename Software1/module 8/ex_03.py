Airport_data_managment = {}

while True:

    print("Airport Data Managment")
    print(f"1. Enter a new airport")
    print(f"2. Fetch airport information")
    print(f"3. Quit")

    command = input(f"Please choose an option (1-3)")

    if command == "1":
        ICAO_code = input("Enter ICAO code: ")
        airport_name = input("Enter airport name: ")
        Airport_data_managment[ICAO_code] = airport_name

    elif command == "2":

        ICAO_code = input("Enter ICAO code")

        if ICAO_code in Airport_data_managment:
                print(f"Airport name: {Airport_data_managment[ICAO_code]}")
        else:
                print(f"Code {ICAO_code} not found")

    elif command == "3":
        print("Thank you for using the Airport Data Managment system. Goodbye!")
        break

    else:
        print("Inavlid choice")