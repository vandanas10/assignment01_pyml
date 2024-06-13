"""program in python that converts a string into a list of its characters."""

char_list = []

input_string = input("Enter a string: ")

for char in input_string:
    char_list.append(char)

print("List of characters:", char_list)
