#Bitwise Operator Tasks 

#1
#Create two variables a = 10 and b = 6, Print the result of a & b.
a = 10
b = 6

print(a & b)

#2
#Create two variables x = 12 and y = 5, Print the result of x | y.
x = 12
y = 5

print(x | y)

#3
#Create a variable num = 8, Print the result of ~num.
num = 8

print(~num)

#4
#Create two variables a = 15 and b = 9, Print the result of a ^ b.
a = 15
b = 9

print(a ^ b)

#5
#Create a variable num = 7, Perform left shift by 2 and print the result.
num = 7
print(num << 2)

#6
# Create a variable num = 20, Perform right shift by 1 and print the result.
num = 20
print(num >> 1)

#7
#Take two numbers from user input and print AND result.
a = int(input("Enter first number:-"))
b = int(input("Enter second number:-"))

result = a & b
print(result)

#8
#Take two numbers from user input and print XOR result.
a = int(input("Enter first number:-"))
b = int(input("Enter second number:-"))

result = a ^ b

print(result)


#String Tasks

#9
#Create a string "hi" and print it 4 times using replication.
a = "hi"

print(a * 4)

#10
# Create a string "python" and print it 3 times.
a = "python"

print(a * 3)

#11
# Create two strings "super" and "man" and combine them using + operator.
str1 = "super"
str2 = "man"

print(str1 + str2)

#12
# Create three strings "hello", " ", "world" and print "hello world".
str1 = "hello"
str2 = " "
str3 = "world"

print(str1 + str2 + str3)


# 13
# Take a name from user input and print it 5 times.
name = input("Enter the Name:-")
print(name * 5)


#14
#Take two strings from user input and concatenate them.
str1 = input("Enter string1:-")
str2 = input("Enter string2:-")

print(str1 + str2)


#Input & Type Casting Tasks

#15
#Take a name from user input and print its data type.
name = input("Enter the name:-")
print("Datatype",type(name))

#16
#Take age from user input and convert it into integer.
age = int(input("Enter your age:- "))

print("Age:", age)
print("Data type:", type(age))

#17
#Take two numbers from user input and print their sum.
num1 = int(input("Enter first number:- "))
num2 = int(input("Enter second number:- "))

print(num1 + num2)

#18
#Take two marks from user input and print their average.
mark1 = float(input("Enter first mark:-"))
mark2 = float(input("Enter second mark:-"))

print((mark1 + mark2) / 2)

#19
#Take two numbers from user input and print 3*a*2 + b - 2.
a = int(input("Enter first numer:-"))
b = int(input("Enter second numer:-"))

print(3*a*2 + b - 2)

#20
#Take a number from user input and print its data type before and after type casting.
num = input("Enter the numer")
print("Before Type Casting:", type(num))

num = int((num))
print("After Type Casting:", type(num))


#Unit Digit Task

#21
#Take a number as string input and print the last digit.
num = input("Enter the numer:")
print(num[len(num)-1])

#22
#Take a number and print the unit digit using % operator.
num = int(input("Enter the numer:"))
print(num % 10)

#23
#Take a number and remove the last digit using // operator.
num = int(input("Enter the numer:"))
print(num // 10)

#24
#Take a number and print the second last digit.
num = int(input("Enter the number:-"))
num //= 10

print(num % 10)

#25
#Take a 5 digit number and print its last digit.
num = int(input("Enter the five digit number:-"))

print(num % 10)


#If statement Task

#26
#Create a program that checks if 10 ≥ 5 and prints a message.
if (10 >= 5):
    print("Condition is True")

#27
#Take a number from user input and check if it is greater than 50.
num = int(input("Enter the number"))

if num > 50:
    print("The number is greater than 50")

#28
#Take age from user input and check if age ≥ 18.
age = int(input("Enter your age:-"))

if age >= 18:
    print("Age is greater than or equal to 18")

#29
#Take a number and check if it is greater than 100.
num = int(input("Enter the number"))

if num > 100:
    print("The number is greater than 100")

#30
#Take a number and check if number ≥ 0.
num = int(input("Enter the number"))

if num >= 0:
    print("The number is greater than or equal to 0")


#If-Else Tasks

#31
#Take a number and check if it is even or odd.
num = int(input("Enter the number:"))

if num %2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#32
#Take marks from user input and check if pass or fail (pass ≥ 35).
num = int(input("Enter your marks:"))

if num >= 35:
    print("PASS")
else:
    print("FAIL")

#33
#Take a number and check if it is positive or negative.
num = int(input("Enter the number:"))

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")

#34
#Take a number and check if it is greater than 10 or not.
num = int(input("Enter the number:"))

if num > 10:
    print("The given number is greater than 10")
else:
    print("The given number is not greater than 10")


#Nested If Tasks

#35
#Create a program for job eligibility:
name = input("Enter your name:")
age = int(input("Enter your age:"))
height = int(input("Enter your height using cm:"))
weight = int(input("Enter your weight using kg:"))

if age >= 18:
    if height >= 160:
        if weight >= 60:
            print(name,"You are Selected for this job")
        else:
            print(name, "Your weight is not eligible, You are Rejected for this job")
    else:
        print(name, "Your height is not eligible, You are Rejected for this job")
else:
    print(name, "Your age is not eligible, You are Rejected for this job")

#36
#Create a college admission program:
name = input("Enter your name:")
marks = int(input("Enter your marks:"))
age = int(input("Enter your age:"))

if marks >= 60:
    if age >= 17:
        print(name,"Your Admission Granted")
    else:
        print(name,"Your age is not eligible, Your Admission Rejected")
else:
    print(name,"Your marks are not eligible, Your Admission Rejected")

#37
#Create a sports selection program:
name = input("Enter your name:")
age = int(input("Enter your age:"))
height = int(input("Enter your height using cm:"))
weight = int(input("Enter your weight using kg:"))

if age >= 16:
    if height >= 150:
        if weight >= 50:
            print(name, "You are Selected for sports")
        else:
            print(name, "Your weight is not eligible, You are Not Selected for sports")
    else:
        print(name, "Your height is not eligible, You are Not Selected for sports")
else:
    print(name, "Your age is not eligible, You are Not Selected for sports")


#Match Statement Task

#38
#Take a number (1-7) and print day name using match.
day = int(input("Enter the day number:"))

match day :
    case 1 :
        print("Sunday")
    case 2 :
        print("Monday")
    case 3 :
        print("Tuesday")
    case 4 :
        print("Wednesday")
    case 5 :
        print("Thursday")
    case 6 :
        print("Friday")
    case 7 :
        print("Saturday")

#39
#Take a number (1-3) and print:
num = int(input("Enter a number (1-3):"))

match num:
    case 1 :
        print("Red")
    case 2 :
        print("Blue")
    case 3 :
        print("Green")

#40
#Take a number (1-4) and print:
num = int(input("Enter the number (1-4):"))

match num:
    case 1 :
        print("Apple")
    case 2 :
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")










