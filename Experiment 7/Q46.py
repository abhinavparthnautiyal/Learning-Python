#Write a Python program to find the key that has the maximum value in a dictionary.
a = {}
num = int(input("Enter the no.of values in your dictionary: "))

for i in range(num):
    a[i] = int(input(f"Enter the value for key {i}: "))

required_key = 0

for key in a:
    if a[key] > a[required_key]:
        required_key = key

print("The key with the greatest value is:", required_key)
