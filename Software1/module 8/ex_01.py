def get_season(month):

   ## winter = ("December", "january", "February")
   ## spring = ("March", "April", "May")
   ## summer = ("June", "July", "August")
   ## autumn = ("September", "October", "November")

    if month in (12, 1, 2):
        return "winter"
    elif month in (3, 4, 5):
        return "spring"
    elif month in (6, 7, 8):
        return "summer"
    elif month in (9, 10, 11):
        return "autumn"
    else:
        return "Please enter a number between 1 and 12."

    
month = int(input("Enter the number of a month (1-12): "))

if month >= 1 and month <= 12:
    print(f"You entered: {month}")
    print(f"The season is {get_season(month)}.")
else:
    print(f"You entered: {month}")
    print(get_season(month))
