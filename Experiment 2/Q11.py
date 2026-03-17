"""Write a Python program using nested if to read marks and display:
Fail if marks < 40
Pass if marks >=40
Distinction if marks >= 75"""
marks=int(input("Enter your marks:"))
if marks<40 :
    print("Fail")
elif marks>=40:
    print("Pass")
    if marks>=75:
         print("Distinct marks")
