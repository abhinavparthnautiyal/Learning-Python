#Write a Python program to convert two lists into a dictionary using one list as keys and the other as values.
a=[1,2,3,4,5,6,7,8]
b=["Hello",",", "How", "are", "you"," ", "?" ,"."]
result={}
for i in range(0,len(a)):
    result[a[i]]=b[i]
print(result)