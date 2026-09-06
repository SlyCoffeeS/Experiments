
username = input("Enter username.")
password = input("Enter password.")

correct_username = "python"
correct_password = "rules"

tries = 2

while username != correct_password and password != correct_password:
    print("Enter the username and password again")
    username = input("Enter username.")
    password = input("Enter password.")

    tries += 1

    if tries > 5:
        print("Acess denied")
        break
    
if username == correct_username and password == correct_password:
        print("Welcome.")