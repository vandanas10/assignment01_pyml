"""program that asks the user for their birth year and calculates their
age."""
from datetime import date
todaydate=date.today()

thisyear=todaydate.strftime("%Y")
birthyear=int(input("enter your birth year: "))
age=int(thisyear)-birthyear

print("your age is : ",age)