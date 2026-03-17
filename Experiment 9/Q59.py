#Write a Python program to sort a list of tuples based on the second element using the sorted() function with a lambda function.
students = [("Alice", 85), ("Bob", 72), ("Charlie", 90), ("David", 65)]

sorted_students = sorted(students, key=lambda x: x[1])

print("Sorted list:", sorted_students)
