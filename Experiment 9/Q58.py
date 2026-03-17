#Write a Python program using a lambda function to find the square of a number entered by the user.
num=int(input("Enter the number whose square you want to find: "))
square=lambda x:x*x
print(square(num))