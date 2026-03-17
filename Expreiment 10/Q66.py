#WAP to copy contents of one file into another file
source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

file1 = open(source, "r")
content = file1.read()
file1.close()

file2 = open(destination, "w")
file2.write(content)
file2.close()

print("File copied successfully!")