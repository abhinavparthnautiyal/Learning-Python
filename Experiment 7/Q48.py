#Write a Python program to remove duplicate values from a dictionary. The resulting dictionary should contain unique values only. Print the same.
a = {1:10,2:20,3:30,4:30,5:40,6:40,7:50,8:66,9:70,10:70,11:88,12:80,13:76,14:50,15:50,16:40}
b = {}

for key in a:
    if a[key] not in b.values():
        b[key] = a[key]

print(b)