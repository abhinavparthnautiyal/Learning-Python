"""Write a Python program that:
Uses filter() to select numbers greater than 10 from a list.
Uses map() with a lambda function to double those numbers."""
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

filtered = list(filter(lambda x: x > 10, numbers))
doubled = list(map(lambda x: x * 2, filtered))

print("Numbers greater than 10:", filtered)
print("Doubled numbers:", doubled)