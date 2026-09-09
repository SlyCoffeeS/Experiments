airports = {}

while True:

    print("\nAirport Data Management")
    print(f"1. Enter a new airport")
    print(f"2. Fetch airport information")
    print(f"3. Quit")

    command = input(f"Please choose an option (1-3): ")

    if command == "1":
        ICAO_code = input("Enter the ICAO code: ")
        airport_name = input("Enter the airport name: ")
        print(f"Airport {airport_name} with ICAO code {ICAO_code} has been added.")
        airports[ICAO_code] = airport_name

    elif command == "2":

        ICAO_code = input("Enter the ICAO code: ")

        if ICAO_code in airports:
                print(f"The airport with ICAO code {ICAO_code} is {airport_name}.")
        else:
                print(f"No airport found with ICAO code {ICAO_code}.")

    elif command == "3":
        print("Thank you for using the Airport Data Management system. Goodbye!")
        break

    else:
        print("Inavlid choice")