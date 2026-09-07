# Question 8: List of 10 student names and their marks

student_names = ["Aman", "Bina", "Chetan", "Divya", "Esha", "Farhan", "Gauri", "Harsh", "Isha", "Jatin"]
student_marks = [78, 92, 55, 88, 67, 45, 99, 73, 61, 84]

print(f"{'Name':<10} {'Marks':<5}")
print("-" * 16)
for i in range(len(student_names)):
    print(f"{student_names[i]:<10} {student_marks[i]:<5}")
