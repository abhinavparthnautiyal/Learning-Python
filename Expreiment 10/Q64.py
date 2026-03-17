#WAP to append data to an existing file using a mode
filename = input("Enter file name: ")
data = input("Enter data to append: ")

file = open(filename, "a")
file.write("\n" + data)
file.close()

print("Data appended successfully!")