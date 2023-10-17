class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    # rather than returning builtin string we can return a custom one
    def __str__(self):
        return f"Person {self.name}"

    # used for dbugger
    def __repr__(self):
        return f"<Person({self.name})>"


stu = Student("Rolf", (90, 90, 93, 78, 90))
print(stu.average())

stu2 = Student("Golf", (90, 90, 93, 78, 90))
print(stu2)
