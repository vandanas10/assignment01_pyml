"""python program that removes all punctuation from a given string."""

import string

def remove_punctuation(input_string):
    punctuation = string.punctuation
    
    result = ""
    
    for char in input_string:
        if char not in punctuation:
            result += char
    
    return result

# main
input_string = input("enter string with punctuations: ")
cleaned_string = remove_punctuation(input_string)

print("Original string:")
print(input_string)

print("\nString with punctuation removed:")
print(cleaned_string)
