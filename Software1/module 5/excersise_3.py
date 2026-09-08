number= input("Enter a number (or press Enter to quit): ")

if number != "":
    number=float(number)
    smallest = number
    largest = number

while number != "":
    number = float(number)

    if smallest > number:
        smallest = float(number)

    elif largest < number:
        largest = number
    number= input("Enter a number (or press Enter to quit): ")

print(f"Smallest number {smallest}")
print(f" Largest number {largest}")