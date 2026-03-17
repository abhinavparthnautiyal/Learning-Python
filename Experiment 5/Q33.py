#WAP to delete all elements greater than 50, count of remaining elements, sort the list, and print the last 3 elements
numbers = [34,546,57,34,676,54,64,22,44,23,59]

for i in numbers:
    if i > 50:
        numbers.remove(i)

numbers.sort()
print(numbers[-3:])

