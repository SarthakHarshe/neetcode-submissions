from typing import List

def read_integers() -> List[int]:
    user_input = input()
    string_list = user_input.split(",")
    for i in range(len(string_list)):
        string_list[i] = int(string_list[i])
    return string_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
