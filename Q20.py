""" python program that takes a list of numbers and returns their sum"""

input_str = input("Enter the list of numbers separated by spaces: ")
list1 = input_str.split() 

list1 = list(map(int, list1))

sum = 0

for number in list1:
    sum += number

print("The sum of numbers in the list:", sum)
