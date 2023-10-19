from typing import List, Optional


class Student:
    # this is bad because parameters are evaluated at the creation of class
    def __init__(self, name, grades: List['int'] = []) -> None:  # This is bad
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)


class Student2:
    def __init__(self, name, grades: Optional[List['int']] = None) -> None:
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


bob2 = Student2("Bob")
rolf2 = Student2("Rolf")
bob2.take_exam(90)
print(bob2.grades)
print(rolf2.grades)
