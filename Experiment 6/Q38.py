"""WAP to count how many elements in a tuple are greater than a given number using the membership concept inside a loop"""
t=tuple(map(int,input("Enter the elements separated by space: ").split()))
x=int(input("Enter the number: "))
count=0
for i in t:
    if i>x:
        count+=1
print(f"In the tuple there are {count} no. of elements which are greater than {x}")

