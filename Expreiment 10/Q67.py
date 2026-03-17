#WAP to count uppercase and lowercase letters in a file
filename = input("Enter file name: ")

file = open(filename, "r")
content = file.read()
file.close()

upper = 0
lower = 0

for char in content:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)