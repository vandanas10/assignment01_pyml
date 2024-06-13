"""program that calculates the sum of the digits of a given
number."""
def sum_of_digits(number):
    sum_digits = 0

    for digit in str(number):
        sum_digits += int(digit)
    
    return sum_digits

#main
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(f"The sum of the digits of {number} is {result}")
