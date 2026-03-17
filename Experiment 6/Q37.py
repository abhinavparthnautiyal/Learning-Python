#WAP to find the index position of a given element in a tuple using index().
t=tuple(map(int,input("Enter elements separated by space: ").split()))
x=int(input("Enter the element to find index: "))
if x in t:
    print("Index position:",t.index(x))
else:
    print("Element not found in tuple")
