
year = float(input("Input a year"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("the year is a leap year")
        else:
            print("the year is not leap year")
else:
            print("the year is not a leap year")