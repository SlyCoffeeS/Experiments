with open("shopping.txt", "r") as myfile:
    file_data = myfile.readlines()
    print(len(file_data))

with open("shopping.txt", "r") as myfile:
    file_data = myfile.read()
    print(file_data)