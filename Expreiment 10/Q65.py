#WAP to write and read a file using w+ mode
filename = input("Enter file name: ")
data = input("Enter data to write: ")

file = open(filename, "w+")
file.write(data)

file.seek(0)
content = file.read()
file.close()

print("Data read from file:", content)