names = set()

while True:
    new_name = input("Enter names")

    if new_name == "":
        break

    if new_name in names:
        print(f"Existing name")

    else:
        names.add(new_name)
        print(f"New name")

for n in names:
    print(n)
