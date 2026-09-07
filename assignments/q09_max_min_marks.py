# Question 9: Find students with maximum and minimum marks

student_names = ["Aman", "Bina", "Chetan", "Divya", "Esha", "Farhan", "Gauri", "Harsh", "Isha", "Jatin"]
student_marks = [78, 92, 55, 88, 67, 45, 99, 73, 61, 84]

max_marks = max(student_marks)
min_marks = min(student_marks)

max_index = student_marks.index(max_marks)
min_index = student_marks.index(min_marks)

print("Student with maximum marks:", student_names[max_index], "-", max_marks)
print("Student with minimum marks:", student_names[min_index], "-", min_marks)
