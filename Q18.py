"""python program that checks if two strings are anagrams of each
other"""
str1=input("enter a first string: ")
str2=input("enter a second string: ")

str1 = str1.lower()
str2 = str2.lower()

# Checking if the strings are anagrams
if sorted(str1) == sorted(str2):
    print("Strings are anagrams.")
else:
    print("Strings are not anagrams.")