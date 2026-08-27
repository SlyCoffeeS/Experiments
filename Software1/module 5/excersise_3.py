number= input("Enter numbers: ")

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
    number= input("Enter a number")

print(f"smallest is  {smallest} and the largest is {largest}")



