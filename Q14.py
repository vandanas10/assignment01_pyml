"""program that reads multiple lines of input from the user until they
enter an empty line, then prints all the lines."""
def read_lines():
    lines = []
    print("Enter multiple lines of text (Enter an empty line to finish):")
    
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    return lines

def print_lines(lines):
    print("\nLines You entered:")
    for line in lines:
        print(line)

# Reading lines from user
user_lines = read_lines()

# Printing the lines entered
print_lines(user_lines)
