#WAP to create a file and write data using w mode
filename = input("Enter file name: ")
data = input("Enter data to write: ")

file = open(filename, "w")
file.write(data)
file.close()

print("Data written successfully!")