# Question 5: Check whether a number is Prime (isPrime function)

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
if isPrime(n):
    print(n, "is a Prime number")
else:
    print(n, "is not a Prime number")
