student_marks={'Alice':85,'Bob':78,'Rocky':90}
student_name=input("Enter the student's name:")
if student_name in student_marks:
    print(f"{student_name}'s marks:{student_marks[student_name]}")
else:
    print("Student not found.")
