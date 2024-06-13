""" program that copies the contents of one text file to another."""

source_file = open("source.txt", "r")

content = source_file.read()

source_file.close()

destination_file = open("destination.txt", "w")

destination_file.write(content)

destination_file.close()

print("File copied successfully!")
