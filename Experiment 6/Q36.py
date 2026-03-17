#WAP to count how many times a specific element appears in a tuple. Input from the user.
t=tuple(map(int,input("Enter the elements separated by space: ").split()))
x=int(input("Enter the element to count: "))
print("The element appears",t.count(x),"times")
