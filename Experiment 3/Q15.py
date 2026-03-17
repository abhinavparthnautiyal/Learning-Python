#WAP to print the multiplication table of a given number using a for loop.
num=int(input("Enter your number:"))
print(f"Table of {num} is as follows:")
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")