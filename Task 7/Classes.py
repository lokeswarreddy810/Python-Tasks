#Task 1: Use super() properly

#Step 1: Parent Class
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(f"Name: {self.name}, ID: {self.id}")

# Step 2: Student Class (inherits User)
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)

        self.dept = dept
        self.fees = fees
    
    def display(self):
        super().display()
        print(f"Department: {self.dept}, Fees: {self.fees}")

# Step 3: Faculty Class (inherits User)
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)

        self.salary = salary

    def display(self):
        super().display()
        print(f"Salary: {self.salary}")

# Step 4: TempFaculty Class (inherits Faculty)
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        
        self.duration = duration

    def display(self):
        super().display()
        print(f"Duration: {self.duration} months")



# Task 2 : Apply Abstraction

from abc import ABC, abstractmethod
 
# Step 1: Create Abstract Base Class
class AbstractUser(ABC):
 
    @abstractmethod
    def get_details(self):
        pass
 
 
# Step 2: User Class (inherits AbstractUser)
class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id
 
    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"
 
 
# Step 3: Student Class
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees
 
    def get_details(self):
        return f"Student -> Name: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"
 
 
# Step 4: Faculty Class
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary
 
    def get_details(self):
        return f"Faculty -> Name: {self.name}, ID: {self.id}, Salary: {self.salary}"
 
 
# Step 5: TempFaculty Class
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration
 
    def get_details(self):
        return f"TempFaculty -> Name: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}"



