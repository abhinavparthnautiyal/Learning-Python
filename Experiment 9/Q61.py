#Write a Python program using the filter() function to extract all even numbers from a given list.
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", even_numbers)