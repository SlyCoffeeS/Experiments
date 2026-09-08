while True:

    enter_inch = float(input("Enter length in inches (negative value to quit): "))

    if enter_inch >= 0:
        print (f"{enter_inch} inches is {enter_inch * 2.54:.2f} centimeters")
    elif enter_inch < 0:
        print("Program ended.")
        break
