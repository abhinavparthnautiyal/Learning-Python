#Write a function fibonacci(n) that returns the nth Fibonacci number using recursion
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
num=int(input("Enter the position at in the fibonacci series at which you want to find the number: "))
print(fibonacci(num))