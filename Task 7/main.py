#Task1: Use super() properly

from Classes import Student, Faculty, TempFaculty

#  Create objects
s = Student("Lokesh", 101, "ECE", 50000)
f = Faculty("Suresh",201, 70000)
t = TempFaculty("Anand", 301, 50000, 6)

# Print output
print("------Student Details------")
s.display()

print("-----Faculty Details------")
f.display()

print("------Temp Faculty Details------")
t.display()



#Task 2: Apply Abstraction

from Classes import Student, Faculty, TempFaculty
 
# Create objects
s1 = Student("Deepu", 101, "CSE", 50000)
f1 = Faculty("Nirvi", 201, 60000)
t1 = TempFaculty("Anvik", 301, 40000, "6 months")
 
# Call get_details()
print(s1.get_details())
print(f1.get_details())
print(t1.get_details())



# # Task 3 : Sorting using key

from Classes import Student, Faculty
 
#  Create list of students
students = [
    Student("Lokesh", 101, "ECE", 50000),
    Student("Ravi", 102, "Civil", 40000),
    Student("Anand", 103, "IT", 60000)
]
 
#Sort students by fees
students.sort(key=lambda x: x.fees)
 
print("Students sorted by fees:")
for s in students:
    print(s.name, s.fees)
 
 
#  Create list of faculty
faculties = [
    Faculty("Siva", 201, 80000),
    Faculty("Anitha", 202, 60000),
    Faculty("Akash", 203, 70000)
]
 
#  Sort faculty by salary
faculties.sort(key=lambda x: x.salary)
 
print("\nFaculty sorted by salary:")
for f in faculties:
    print(f.name, f.salary)



# # Task 4 : Use map()

from Classes import Student, Faculty
 
#  Create list of students
students = [
    Student("Lokesh", 101, "CSE", 50000),
    Student("Anil", 102, "ECE", 40000),
    Student("Balu", 103, "IT", 60000)
]
 
# Use map() to extract names
names = list(map(lambda s: s.name, students))
 
# Step 3: Print result
print("Student Names:")
print(names)


# # Task 5 : Use filter()

from Classes import Student, Faculty
 
# Create students list
students = [
    Student("Lokesh", 101, "CSE", 50000),
    Student("Anil", 102, "ECE", 40000),
    Student("Balu", 103, "IT", 60000)
]
 
# Filter students with fees > 50000
high_fee_students = list(filter(lambda s: int(s.fees) > 50000, students))
 
print("Students with fees > 50000:")
for s in high_fee_students:
    print(s.name, s.fees)
 
 
# Create faculty list
faculties = [
    Faculty("Siva", 201, 80000),
    Faculty("Anitha", 202, 60000),
    Faculty("Akash", 203, 70000)
]
 
# Filter faculty with salary > 30000
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculties))
 
print("\nFaculty with salary > 30000:")
for f in high_salary_faculty:
    print(f.name, f.salary)



# #Task 6 : Use reduce()

from Classes import Student, Faculty
from functools import reduce
 
#  Create students list
students = [
    Student("Lokesh", 101, "CSE", 50000),
    Student("Anil", 102, "ECE", 40000),
    Student("Balu", 103, "IT", 60000)
]
 
# Calculate total fees using reduce()
total_fees = reduce(lambda acc, s: acc + int(s.fees), students, 0)
 
print("Total Fees Collected:", total_fees)
 
 
#  Create faculty list
faculties = [
    Faculty("Siva", 201, 80000),
    Faculty("Anitha", 202, 60000),
    Faculty("Akash", 203, 70000)
]
 
#Calculate total salary using reduce()
total_salary = reduce(lambda acc, f: acc + f.salary, faculties, 0)
 
print("Total Salary of Faculty:", total_salary)



# #Task 7 : Higher Order Function


from Classes import Student, Faculty
 
#  Higher Order Function
def process_users(users, func):
    return list(map(func, users))
 
 
# Create students list
students = [
    Student("Lokesh", 101, "CSE", 50000),
    Student("Anil", 102, "ECE", 40000),
    Student("Balu", 103, "IT", 60000)
]
 
#  Use function to extract names
names = process_users(students, lambda s: s.name)
 
print("Student Names:")
print(names)
 
 
# Use function to extract fees
fees = process_users(students, lambda s: s.fees)
 
print("\nStudent Fees:")
print(fees)
 
 
# Create faculty list
faculties = [
    Faculty("Siva", 201, 80000),
    Faculty("Anitha", 202, 60000),
    Faculty("Akash", 203, 70000)
]
 
# Extract salaries
salaries = process_users(faculties, lambda f: f.salary)
 
print("\nFaculty Salaries:")
print(salaries)
 


# # Final Challenge
 
from Classes import Student, Faculty
from functools import reduce
 
# Higher Order Function
def process_users(users, func):
    return list(map(func, users))
 
 
# Create Data
students = [
   Student("Lokesh", 101, "CSE", 50000),
   Student("Anil", 102, "ECE", 40000),
   Student("Balu", 103, "IT", 60000)
]
 
faculties = [
    Faculty("Siva", 201, 80000),
    Faculty("Anitha", 202, 60000),
    Faculty("Akash", 203, 70000)
]
 
 
#Print All Details (Abstraction)
print("----- ALL DETAILS -----")
for s in students:
    print(s.get_details())
 
for f in faculties:
    print(f.get_details())
 
 
#Sorting (key + lambda)
students.sort(key=lambda s: s.fees)
faculties.sort(key=lambda f: f.salary)
 
print("\n----- SORTED DATA -----")
print("Students (by fees):")
for s in students:
    print(s.name, s.fees)
 
print("Faculty (by salary):")
for f in faculties:
    print(f.name, f.salary)
 
 
#Filtering (filter + lambda)
high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculties))
 
print("\n----- FILTERED DATA -----")
print("High Fee Students:")
for s in high_fee_students:
    print(s.name, s.fees)
 
print("High Salary Faculty:")
for f in high_salary_faculty:
    print(f.name, f.salary)
 
 
#Map (extract names using higher order function)
student_names = process_users(students, lambda s: s.name)
print("\nStudent Names:", student_names)
 
 
# Reduce (total calculation)
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculties, 0)
 
print("\n----- TOTALS -----")
print("Total Fees:", total_fees)
print("Total Salary:", total_salary)