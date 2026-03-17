#WAP to count the number of vowels and consonants in a given string.
string = input("Enter your string: ")
vowels = 0
consonants = 0

for c in string:
    if c in "aeiouAEIOU":
        vowels += 1
    elif c == " ":
        continue
    else:
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)