#Write a Python program to count the frequency of each character in a given string using a dictionary.
string=input("Enter your string: ")
frequency={}
for ch in string:
    if ch in frequency:
        frequency[ch]+=1
    else:
        frequency[ch]=1
print(frequency)
