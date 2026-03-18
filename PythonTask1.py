# Task1 - Printing Formating

print("Hello world", end=" ")
print("Welcome Python")

print("Laptop","Mouse","Keyboard", sep="|")

# Task2 - Variables

name = "Ravi"
age = 22
city = "Chennai"

print(name,age,city, sep="-")

# Task3 - Multiple Assignment

name,age,student = "Meena",20, True

print("multi assignment :-",name,age,student)

# Task4 - Indexing

word = "Python"

print(word[0])
print(word[2])
print(word[5])

# Task5 - Arithmetic Operators

#1
a = 25
b = 10

print(a+b)

#2
a = 50
b = 20

print(a-b)

#3
a = 8
b = 5

print(a*b)

#4
a = 100
b = 10

print(a/b)

#5
a = 10
b = 3

print(a%b)

#6
a = 2
b = 4

print(a**b)

#7
a = 20
b = 3

print(a//b)

# Task6 - BODMAS Expression
 
print(3+2*5**2)

# Task7 - Assignment Operator

num = 50
num += 25

print(num)

num = 100
num /= 10

print(num)

# Task8 - Comparison Operators

a = 10
b = 5

print(a>b)

a = 20
b = 15

print(a<b)

a = 5
b = 5

print(a==b)

a = 10
b = 8

print(a!=b)

a = 7
b = 7

print(a>=b)

a = 6
b = 2

print(a<=b)

# Task9 String Comparison 

a = "apple"
b = "Apple"

print("String Comparsion:",a==b)


# Task10 - Logical Operator

print(10>5 and 5==5)
print(5>10 or 10==10)
print(not(5>2))

# Task 11 – Membership Operator
numbers = [10,20,30,40,50]

# 20 in numbers
print(20 in numbers)

# 60 in numbers
print(60 in numbers)

# 30 not in numbers
print(30 not in numbers)

# Task 12 – Swap Variables
a = 10
b = 20

temp = a
a = b
b = temp

print("a =",a)
print("b =",b)

# Task 13 – Bitwise XOR
a = 6
b = 3

print(a ^ b)


