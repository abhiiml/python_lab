# Find the largest of four numbers
a1 = int(input("enter first: "))
a2 = int(input("enter second: "))
a3 = int(input("enter third: "))
a4 = int(input("enter fourth: "))

if a1 >= a2 and a1 >= a3 and a1 >= a4:
    print("first is largest:", a1)
elif a2 >= a1 and a2 >= a3 and a2 >= a4:
    print("second is largest:", a2)
elif a3 >= a1 and a3 >= a2 and a3 >= a4:
    print("third is largest:", a3)
else:
    print("fourth is largest:", a4)