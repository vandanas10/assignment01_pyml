"""program that takes a string input from the user and writes it to a
text file."""
str=input("enter a string: ")
file1=open("firstText.txt","w")
file1.write(str)
file1.close()