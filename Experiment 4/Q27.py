#WAP to extract the middle 3 characters from a given string using slicing.
string = input("Enter a string: ")
mid=len(string)//2
print("The middle three words are as follows",string[mid-1:mid+2])