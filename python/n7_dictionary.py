student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student in student_attendance:
    print(student)

for student, attendance in student_attendance.items():
    print(student, attendance)
