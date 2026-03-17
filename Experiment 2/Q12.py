"""Write a program that determines loan eligibility based on age and monthly income.
The person must be at least 21 years old.If they are eligible by age, check if their income is at least $30,000.
If both conditions are met, print "You are eligible for the loan."
Otherwise, print "Income insufficient for loan eligibility." """

age=int(input("Enter your age:"))

income=int(input("Enter your monthly income:"))
if age>=21:
    if income>=30000:
        print("You are eligible for loan")
    else :
        print("You are not eligible for loan due to income insufficiency")
else:
    print("You are not eligible for loan due to age")