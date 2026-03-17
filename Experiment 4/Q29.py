#WAP to print the result of multiplication inside an f-string.
num=int(input('Enter the number whose table you want to find: '))
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")