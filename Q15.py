"""program that reads data from a CSV file and prints it to the
console."""
import csv
filecsv=open("firstcsv.csv","r")
csv_reader=csv.reader(filecsv)
for row in csv_reader:
        print(" ".join(row))