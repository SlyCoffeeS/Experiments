Gender = str(input("whats your gender ")).lower()


if Gender == "male":
    hemoglobin_value = float(input("Enter hemogloblin value "))
    if hemoglobin_value < 134:
        print("hemogloblin value is low")
    elif hemoglobin_value > 167:
        print("Hemogloblin value is High")
    elif hemoglobin_value >= 134 and hemoglobin_value <= 167 :
        print("Hemogloblin value is normal")

if Gender == "female":
    hemoglobin_valuefemale = float(input("Enter hemogloblin value "))
    if hemoglobin_valuefemale < 117:
        print("Hemogloblin value is low")
    elif hemoglobin_valuefemale >= 117 and hemoglobin_valuefemale <= 155 :
        print("Hemogloblin value is normal")
    elif hemoglobin_valuefemale > 155:
        print("Hemogloblin value is high")
    
