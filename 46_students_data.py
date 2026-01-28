students=[input("Enter student name: ") for _ in range(3)]
marks=[float(input(f"Enter marks for {student}: ")) for student in students]
students_details=dict(zip(students, marks))
below_average_students={student:mark for student,mark in students_details.items() if mark<sum(marks)/len(marks)}
top_students={student:mark for student,mark in students_details.items() if mark>=(sum(marks)/len(marks))}
print("Students scoring below average:")
for student, marks in below_average_students.items():
    print(f"{student}: {marks}")
print("Top scoring students:")
for student, marks in top_students.items():
    print(f"{student}: {marks}")
