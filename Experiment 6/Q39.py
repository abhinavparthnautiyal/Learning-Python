#WAP to convert a tuple into a list, modify one element, and convert it back to a tuple.
t=tuple(map(int,input("Enter the elements of the tuple separated by space: ").split()))
print(t)
lst=list(t)
pos=int(input("Enter the position you want to modify: "))
new_num=int(input("Enter the new element you want to change: "))
lst[pos]=new_num
t=tuple(lst)
print(t)
