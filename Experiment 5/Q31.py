#WAP to delete the first and last elements if the list length is greater than 5, else append the sum of all elements, then sort and print the reversed list using slicing.
numbers = [1,2,3,4,5,6]
sum =0
length = len(numbers)
if length > 5 :
   del numbers[-1]
   del numbers[0]
else:
    for i in numbers:
        sum += numbers[i]
    numbers.append(sum)
    numbers.sort()
print(numbers[::-1])