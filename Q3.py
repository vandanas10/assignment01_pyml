""" python program that calculates the factorial of a given number"""

def calculate_factorial(num):

    factorial = 1

    if num < 0:
        return None  
    elif num == 0:
        return 1  
    else:
        for i in range(1, num + 1):
            factorial *= i
        
        return factorial

# main
num = int(input("Enter a number to calculate its factorial: "))

result = calculate_factorial(num)

if result is None:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {result}.")
