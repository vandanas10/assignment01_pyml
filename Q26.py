""" program in python that checks if a string starts with a given prefix
or ends with a given suffix"""

def check_prefix_suffix(input_string, prefix, suffix):
    starts_with_prefix = input_string.startswith(prefix)
    ends_with_suffix = input_string.endswith(suffix)
    
    if starts_with_prefix:
        print(f"The string '{input_string}' starts with the prefix '{prefix}'.")
    else:
        print(f"The string '{input_string}' does not start with the prefix '{prefix}'.")
        
    if ends_with_suffix:
        print(f"The string '{input_string}' ends with the suffix '{suffix}'.")
    else:
        print(f"The string '{input_string}' does not end with the suffix '{suffix}'.")

# main
input_string = "Hello, World!"
prefix = "Hello"
suffix = "World!"

check_prefix_suffix(input_string, prefix, suffix)
