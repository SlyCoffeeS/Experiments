Gender = str(input("Enter biological gender (male/female): ")).lower()


if Gender == "male":
    hemoglobin_value = float(input("Enter hemoglobin value (g/l): "))
    if hemoglobin_value < 134:
        print("Your hemoglobin is low. ")
    elif hemoglobin_value > 167:
        print("Your hemoglobin is high. ")
    elif hemoglobin_value >= 134 and hemoglobin_value <= 167 :
        print("Your hemoglobin is normal. ")

elif Gender == "female":
    hemoglobin_valuefemale = float(input("Enter hemoglobin value (g/l): "))
    if hemoglobin_valuefemale < 117:
        print("Your hemoglobin is low. ")
    elif hemoglobin_valuefemale >= 117 and hemoglobin_valuefemale <= 155 :
        print("Your hemoglobin is normal. ")
    elif hemoglobin_valuefemale > 155:
        print("Your hemoglobin is high. ")

else:
    value = input("Enter hemoglobin value (g/l): ")
    print("Invalid gender. ")
    
