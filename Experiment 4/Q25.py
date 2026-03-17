#WAP to print the first 5 characters of a given string using slicing.
string=input("Enter your string: ")
if len(string)<4:
    print("The string does not have 5 characters")
else:
    print(f"The first five characters of the string are: {string[:5]}")
