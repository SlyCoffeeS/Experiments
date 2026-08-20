import math

talents = input("Enter talents: ")
pounds = input("Enter pounds: ")
lots = input("Enter lots: ")

talents = float(talents)
pounds = float(pounds)
lots = float(lots)

total_grams = talents * 20 * 32 * 13.3 + pounds * 32 * 13.3 + lots * 13.3
kilogram = int(total_grams)

kilograms = (kilogram / 1000)
kilograms = int(kilograms)
remaining_grams = float(total_grams % 1000)

print(f"The weight in modern units:")
print(f"{kilograms} kilograms and {remaining_grams:3.2f} grams.")