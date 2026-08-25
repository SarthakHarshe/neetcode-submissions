def add_two_numbers() -> int:
    num_input = input()
    num_list = num_input.split(",")
    sum = 0
    for element in num_list:
        sum += int(element)
    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
