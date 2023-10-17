student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

print(list(student_attendance.items()))

a, b, c, d = [1, 2, 3, 5]

print(a, b, c, d)

head, *tail = ["a", "b", "c", "d"]

print(head, tail)

*head, tail = ["a", "b", "c", "d"]

print(head, tail)
