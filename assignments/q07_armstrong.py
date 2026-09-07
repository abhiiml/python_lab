# Question 7: Check Armstrong number (checkArmstrong function)

def checkArmstrong(num):
    digits = str(abs(num))
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == num

n = int(input("Enter a number: "))
if checkArmstrong(n):
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")
