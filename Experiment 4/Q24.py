#WAP to check whether a given string is a palindrome or not.
string=input("Enter your string: ")
reverse_string=""
for i in range(len(string)-1, -1, -1):
    reverse_string += string[i]
print(reverse_string)
if string==reverse_string:
    print("Yes, it is palindrome")
else:
    print("Not palindrome")