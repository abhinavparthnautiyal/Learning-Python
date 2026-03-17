#Write a function factorial(n) that calculates the factorial of a number using recursion
def factorial(n):
    if n==1 or n==0:
        return 1
    return n * factorial(n-1)
num=int(input("Enter the number whose factorial you want to find: "))
print(factorial(num))