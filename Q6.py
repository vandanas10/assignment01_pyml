"""program that reads the content of a text file and prints it to the
console"""
myfile=open(r"D:\imp\pyML\firstText.txt","r")
str=myfile.read()
print(str)
myfile.close()