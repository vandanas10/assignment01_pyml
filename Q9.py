"""program that checks if a substring is present in a given
string."""
str=input("enter a string: ")
substr=input("enter a substring: ")
res=substr in str
print("Is substr present in str?: ",res)