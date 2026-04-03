class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(f"Name: {self.name}, ID: {self.id}")


class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)

        self.dept = dept
        self.fees = fees
    
    def display(self):
        super().display()
        print(f"Department: {self.dept}, Fees: {self.fees}")

class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)

        self.salary = salary

    def display(self):
        super().display()
        print(f"Salary: {self.salary}")

class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        
        self.duration = duration

    def display(self):
        super().display()
        print(f"Duration: {self.duration} months")


