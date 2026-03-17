"""WAP to check whether a given number is a prime number using if and for loop."""
num=int(input("Enter the number you want to check:"))
count=0
if num > 1:
  for i in range(1,num+1):
      if num%i==0:
          count+=1
if count==2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

