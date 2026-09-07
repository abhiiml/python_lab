# Question 6: Sum of digits of a number (doSum function)

def doSum(num):
    num = abs(num)
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

n = int(input("Enter a number: "))
print("Sum of digits of", n, "is", doSum(n))
