def gallons_to_liters(gallons):
    return gallons * 3.785


gallons = float(input("Enter a volume in American gallons (negative value to quit): "))

while gallons >= 0:
    result = gallons * 3.785
    print(f"{gallons} American gallons is {result:.2f} liters.")

    gallons = float(input("Enter a volume in American gallons (negative value to quit): "))


print("Program finished")