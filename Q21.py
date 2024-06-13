"""python program that counts the occurrences of a specific element
in a list."""

def count_freq(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

# main
input_list = [1, 2, 3, 4, 2, 2, 5, 2]
element_to_count = 2

freq = count_freq(input_list, element_to_count)

print(f"The element {element_to_count} occurs {freq} times in the list.")
