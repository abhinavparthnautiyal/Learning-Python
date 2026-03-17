#Write a Python program using the map() function to convert a list of temperatures from Celsius to Fahrenheit.
celsius = list(map(float, input("Enter temperatures in Celsius separated by space: ").split()))

fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print("Fahrenheit:", fahrenheit)