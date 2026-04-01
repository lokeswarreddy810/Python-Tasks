#Task 1: Encapsulation (User Class)
 
class User:
    def __init__(self):
        self.__user_name = None
        self.__pwd = None
 
    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd
 
    def get_user(self):
        return self.__user_name
   
    def register(self):
        print(f"Registering user: {self.__user_name}")
 
    def login(self):
        print(f"Logging in: {self.__user_name}")
 
 
user = User()
user.set_user("John", "8106")
user.register()
user.login()
 
 
#Task 2: Inheritance (User → Student, Faculty)
 
class User:
    def register(self):
        print("User Registered")
 
    def login(self):
        print("User Logged In")
 
class Student(User):
    def student_greet(self):
        print("Hi Student")
 
class Faculty(User):
    def faculty_greet(self):
        print("Hi Faculty")
 
class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")
 
s = Student()
s.register()
s.login()
s.student_greet()
 
f = Faculty()
f.register()
f.faculty_greet()
 
t = TempFaculty()
t.login()
t.faculty_greet()
t.tempFaculty_greet()
 
# Task 3: Method Overriding
 
class User:
    def greet(self):
        print("Welcome User")
 
class Student:
    def greet(self):
        print("Welcome Student")
 
class Faculty():
    def greet(self):
        print("Welcome Faculty")
 
 
s = Student()
f = Faculty()
 
s.greet()
f.greet()
 
 
#Task 4: Method Chaining
 
class User:
    def register(self):
        print("Registered")
        return self
   
    def login(self):
        print("Logined")
        return self
 
    def greet(self):
        print("Enjoy Everyone")
        return self
   
user = User()
user.login().greet().register()
 
 
#Task 5: Combined Task (Real-Time)
class User:
    users_count = 0
 
    def __init__(self, name, pwd):
        self.__name = name
        self.__pwd = pwd
        User.users_count += 1
 
    def get_name(self):
        return self.__name
   
    def register(self):
        print(f"{self.__name} registered")
        return self
 
    def login(self):
        print(f"{self.__name} logged in")
        return self
   
    def greet(self):
        print("Welcome User")
        return self
   
class Student(User):
    def greet(self):
        print("Welcome Student")
        return self
   
class Faculty(User):
    def greet(self):
        print("welcome Faculty")
        return self
   
 
s1 = Student("Lokesh", "8106")
f1 = Faculty("admin", "admin1234")
 
s1.login().greet().register()
f1.login().greet().register()
 
print("Total Users:", User.users_count)