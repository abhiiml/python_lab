# Question 4: Factorial of a number using a function

def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
res = factorial(num)
if res is None:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", num, "is", res)
