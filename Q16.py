""" program in python that counts the frequency of each character in
a string"""
str=input("enter a string: ")
char_freq={}
count=0
for character in str:
    if character in char_freq:
        char_freq[character] += 1
    else:
        char_freq[character] = 1

print(char_freq)