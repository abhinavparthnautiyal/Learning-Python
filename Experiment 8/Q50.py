"""Write a program that defines a function sum_even(n) which:
Uses a loop to iterate from 1 to n
Uses an if condition to check for even numbers
Returns the sum of all even numbers"""
def sum_even(n):
    sum=0
    for i in range (1, n+1):
        if i % 2 == 0:
            sum+=i
    return sum
num=int(input("Enter the number upto which you want to find the sum of even numbers starting from 1: "))
sum=sum_even(num)
print(sum)