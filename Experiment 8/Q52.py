"""Write a function print_primes(n) that:
Uses loops to check numbers from 2 to n
Uses if conditions to determine whether a number is prime
Prints all prime numbers up to n"""
def print_primes(n):
    for i in range(2,n+1):
        isprime=True
        for j in range(2,i):
            if i%j==0:
                isprime=False
        if isprime:
            print(i, end=' ')

num=int(input("Enter the number upto which you want to print all the prime numbers starting from 2: "))
print_primes(num)