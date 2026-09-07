# 2D Array Assignment using NumPy
import numpy as np

# 2D array of marks
# Student 0, Student 1, Student 2, Student 3, Student 4
marks = np.array([
    [80, 70, 90],
    [60, 75, 85],
    [90, 88, 95],
    [55, 65, 70],
    [78, 82, 80]
])

print("Marks Matrix:\n", marks)

# i. Maximum marks
print("\ni. Maximum marks:", np.max(marks))

# ii. Minimum marks
print("ii. Minimum marks:", np.min(marks))

# iii. Average marks
print(f"iii. Average marks: {np.mean(marks):.2f}")

# iv. Maximum marks subject-wise
print("iv. Maximum marks subject-wise:", np.max(marks, axis=0))

# v. Average marks subject-wise
print("v. Average marks subject-wise:", np.mean(marks, axis=0))

# vi. Add 10 marks to students who scored less than 50 in Subject 1
for i in range(len(marks)):
    if marks[i][0] < 50:
        marks[i][0] += 10
print("vi. Marks after grace addition:", marks)

# vii. Number of students who scored more than 80 in Subject 2
count = sum(1 for row in marks if row[1] > 80)
print("vii. Number of students with >80 in Subject 2:", count)

# viii. Minimum marks of Student 2 (third student)
print("viii. Minimum marks of Student 2:", np.min(marks[2]))
