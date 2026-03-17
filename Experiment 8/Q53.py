"""Write a function find_max(numbers) which:
Uses a loop to iterate through the list
Uses if condition to compare numbers
Returns the largest number"""
def find_max(numbers):
    largest=0
    for i in numbers:
            if i>largest:
                largest=i
    return largest

num=list(map(int,input("Enter the numbers to be entered in the list separated by space: ").split()))
print("The largest number is: ", find_max(num))