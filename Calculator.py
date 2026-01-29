print("--- UPES Python Lab: Calculator ---")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect Operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("\nEnter choice (1/2/3/4): ")

if choice == '1':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif choice == '2':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif choice == '3':
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error! Division by zero.")

else:
    print("Invalid Input!")