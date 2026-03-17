"""Write a program that defines a function count_vowels(text) which:
Uses a loop to go through each character
Uses an if condition to check if it is a vowel (a, e, i, o, u)
Returns the total number of vowels"""

def count_vowels(str):
    count=0
    for i in str:
        if i in "aeiouAEIOU":
            count+=1
    return count

str1=input("Enter the sentence: ")
count=count_vowels(str1)
print("The number of vowels in the sentence is: ",count)
