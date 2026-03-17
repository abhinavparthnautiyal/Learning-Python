#Write a recursive function sum_digits(n) that finds the sum of digits of a number.
def sum_digits(n):
    sum=0
    while n>0:
        temp=n%10
        sum+=temp
        n=n//10
    return sum
num=int(input("Enter the number whose sum of digits you want to find: "))
print(sum_digits(num))