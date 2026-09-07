# Question 10: Operations on a list of 20 student marks
from statistics import mode

marks = [78, 92, 55, 88, 67, 45, 99, 73, 61, 84,
         55, 67, 90, 88, 73, 40, 67, 85, 92, 60]

# 1. Average marks
average = sum(marks) / len(marks)
print("Average marks:", round(average, 2))

# 2. Number of students scoring more than average
count_above = sum(1 for m in marks if m > average)
print("Number of students above average:", count_above)

# 3. Marks scored by maximum number of students
most_common_mark = mode(marks)
print("Marks scored by maximum students (mode):", most_common_mark)
