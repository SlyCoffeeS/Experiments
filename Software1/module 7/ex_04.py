def sum_of_list(numbers):
    total = 0

    for n in numbers:
        total += n

    return total

number_list = [1, 2, 3, 4, 5]
result = sum_of_list(number_list)

print(f"The sum of the numbers in the list is: {result}")