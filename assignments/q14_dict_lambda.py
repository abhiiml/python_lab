# Question 14: Dictionary and Lambda Functions
# Define a dictionary student where roll number is the key and the value is another dictionary
# containing name, department and marks.

student = {
    1: {"name": "A", "dept": "CSE", "marks": 80},
    2: {"name": "B", "dept": "IT", "marks": 90},
    3: {"name": "C", "dept": "CSE", "marks": 70},
    4: {"name": "D", "dept": "ECE", "marks": 85},
    5: {"name": "E", "dept": "IT", "marks": 95}
}

# (i) Sort the dictionary according to marks, high to low
sorted_by_marks = sorted(student.items(), key=lambda x: x[1]["marks"], reverse=True)
print("(i) Sorted by marks (high to low):")
for roll, info in sorted_by_marks:
    print(f"  Roll {roll}: {info}")

# (ii) Print the record of the student who scored maximum marks
top_student = max(student.items(), key=lambda x: x[1]["marks"])
print("\n(ii) Student with maximum marks:")
print(f"  Roll {top_student[0]}: {top_student[1]}")

# (iii) Find the average marks of the students
total_marks = sum(record["marks"] for record in student.values())
avg_marks = total_marks / len(student)
print(f"\n(iii) Average marks of students: {avg_marks:.2f}")

# (iv) Print the records of the students who scored more than the average marks
print(f"\n(iv) Students who scored more than average ({avg_marks:.2f}):")
for roll, info in student.items():
    if info["marks"] > avg_marks:
        print(f"  Roll {roll}: {info}")
