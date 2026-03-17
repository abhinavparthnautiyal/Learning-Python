"""Write a program that defines a function factorial(n) which:
Uses an if condition to check if n is negative
Uses a loop to calculate factorial
Returns the factorial value"""
def factorial(n):
    factorial=1
    if n<0:
        print("n is negative")
        return
    elif n==0:
        pass
    else:
        for i in range(1,n+1):
            factorial=factorial*i
    return factorial


num=int(input("Enter the number whose factorial you want to find: "))
print(factorial(num))