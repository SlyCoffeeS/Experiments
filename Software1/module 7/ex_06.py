import math

def calculate_unit_price(diameter, price):
    area = math.pi * (diameter / 2) ** 2
    return price / (area / 10000)


diameter1 = float(input("Enter the diameter of the first pizza (cm): "))
price1 = float(input("Enter the price of the first pizza (euros): "))
diameter2 = float(input("Enter the diameter of the second pizza (cm): "))
price2 = float(input("Enter the price of the second pizza (euros): "))

pizza1 = calculate_unit_price(diameter1, price1)
pizza2 = calculate_unit_price(diameter2, price2)
print(f"Unit price of the first pizza: {pizza1:.2f} euros/m²")
print(f"Unit price of the second pizza: {pizza2:.2f} euros/m²")

if pizza1 < pizza2:
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")