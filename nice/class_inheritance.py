class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property  #decorator - can call def weekly_salary without ()
    # cannot use with an action or argument other than 'self'
    def weekly_salary(self):
        return self.salary * 37.5


rolf = WorkingStudent('Rolf', 'MIT', 15.50)
print(rolf.salary)
rolf.marks.append(57)
rolf.marks.append(99)
print(rolf.average())
# print(rolf.weekly_salary()) # cannot call with () due to decorator
print(rolf.weekly_salary)
