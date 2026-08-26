fish_size = input("Enter the length of the zander in centimeters: ")

fish_size = float(fish_size)

if fish_size >= 42:
    print("The zander meets the size limit. ")

if fish_size < 42:
    print ("The zander does not meet the size limit. ")
    print ("Please release the fish back into the lake. ")
    print(f"The fish was {42 - fish_size:.1f} centimeters below the size limit. ")