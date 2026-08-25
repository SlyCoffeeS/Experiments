

cabin_class = input("Input cabin class").lower()

cabin_class = str(cabin_class)


    
if cabin_class == "lux":
        print("LUX: upper-deck cabin with a balcony")
elif cabin_class == "a":
        print("A: above the car deck, equipped with a window")
elif cabin_class == "b":
        print("B: windowless cabin above the car deck")
elif cabin_class == "c":
        print("C: windowless cabin below the car deck")
else:
        print("Invalid cabin class.")