#WAP to count the number of digits in a given integer using a while loop
num=int(input("Enter a number:"))
number=num
count=0
if num==0:
    count=1
else:
    while num>0:
        num=num//10
        count+=1
print(f"The integer({number}) has {count} digits")