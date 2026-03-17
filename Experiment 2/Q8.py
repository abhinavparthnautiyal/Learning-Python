#Write a Python program that accepts an integer from the user and checks whether the number is positive, negative, or zero.
num=int(input("Enter the integer: "))
if num<0 :
    print("The number is negative")
elif num==0 :
    print("The number is zero")
else :
    print("The number is positive")