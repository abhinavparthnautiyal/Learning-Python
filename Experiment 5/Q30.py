#WAP to insert 50 at the middle index if the list length is even, else append 100, then sort and print the first 4 elements using slicing.
numbers = [10, 20, 30, 40, 60, 70]

length = len(numbers)

if length % 2 == 0:
    mid_index = length // 2
    numbers.insert(mid_index, 50)
else:
    numbers.append(100)

numbers.sort()

print("Processed List:", numbers[:4])