def get_season(month):

    Winter = ("December", "january", "February")
    Spring = ("March", "April", "May")
    Summer = ("June", "July", "August")
    Autumn = ("September", "October", "November")

    if month in (12, 1, 2):
        return "Winter"
    elif month in (3, 4, 5):
        return "Spring"
    elif month in (6, 7, 8):
        return "Summer"
    elif month in (9, 10, 11):
        return "Autumn"
    else:
        return "Invalid month"

    
month = int(input("Enter number of a month"))
print(get_season(month))