#WAP to create an empty set and add 5 elements into it using the add() method. Then display the final set.
s=set()
for i in range(5):
    x=int(input(f"Enter the {i+1} element: "))
    s.add(x)
print(s)

