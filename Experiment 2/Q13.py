"""Write a Python program to determine a student’s result based on the following conditions:
The student passes only if the score is 60 or above.
If the student passes, check whether attendance is at least 80%.
If attendance is sufficient, check whether the assignment has been submitted.
If submitted, display “Pass with good standing”.
If not submitted, display “Pass but missing assignment”.
If attendance is below 80%, display “Pass but low attendance”.
If the score is below 60, display “Fail”.
Use nested if–else statements to implement the program."""
marks=int(input("Enter your marks: "))
attendance=int(input("Enter your attendance in %: "))
assignment=input("Enter if assignment is submitted (yes/no): ").lower()
Pass_flag=True
if marks>=60:
    if attendance>=80:
        if assignment=="yes":print("Pass with good standing")
        else:print("Pass but missing assignment")
    else:print("Pass but low attendance")
else:
    Pass_flag=False
    print("Fail")

