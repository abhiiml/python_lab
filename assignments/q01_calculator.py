# Question 1: Calculator
# Write a Python program to take two numbers from the user and perform addition, subtraction, multiplication and division.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
if b != 0:
    print("Division:", a / b)
else:
    print("Division: Cannot divide by zero")
