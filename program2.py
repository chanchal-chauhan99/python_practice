# Prompt the user to input two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Swap the values using arithmetic operations
number1 = number1 + number2
number2 = number1 - number2
number1 = number1 - number2

# Print the swapped values
print("After swapping:")
print(f"First number: {number1}")
print(f"Second number: {number2}")
