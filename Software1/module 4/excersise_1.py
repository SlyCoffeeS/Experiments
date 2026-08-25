
fish_size = input('Whats the length of the zander?')

fish_size = int(fish_size)

if fish_size >= 42:
    print("Keep the fish")

if fish_size <= 41:
    print(f"the fish is {42 - fish_size} cm too small")