"""WAP to create a list of numbers from 1 to 20.
Using a nested for loop:
Skip (do not add) numbers that are divisible by 3 using continue
Stop the program completely when the number 15 is encountered using break
Store only the remaining numbers in a list
Finally, print the list"""
filtered_numbers = []
for num in range(1, 21):
    if num == 15:
        break
    if num % 3 == 0:
        continue
    filtered_numbers.append(num)
print("Filtered List:", filtered_numbers)