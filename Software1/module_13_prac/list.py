with open("shopping.txt", "w") as myfile:
    myfile.write("milk\njam\nbread\njuice")
with open("shopping.txt", "a") as myfile:
    myfile.write("\ncoke")