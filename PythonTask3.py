# Section 1: Loop Basics

# 1. Print numbers from 1 to 50 using for loop

for i in range(1, 51):
    print(i)

# 2. Print even numbers from 1 to 100

for i in range(1, 101):
    if i % 2 == 0:
        print(i)

# 3. Print odd numbers from 1 to 100

for i in range(1, 101):
    if i % 2 != 0:
        print(i)

# 4. Print multiplication table of 7

for i in range(1, 11):
    print("7 x ", i, " = ", 7* i)

# 5. Find sum of numbers from 1 to 100

total = 0
for i in range(1,101):
    total += i
    print(total)

# 6. Print numbers in reverse from 50 to 1

for i in range(51, 0, -1):
    print(i)

# 7. Count how many numbers are divisible by 3 (1–100)

count = 0

for i in range(1, 101):
    if i % 3 == 0:
        count += 1
print("Count = ", count)

# 8. Print squares of numbers from 1 to 10

for i in range(1, 11):
    print(i * i)

# 9. Print cube of first 10 numbers

for i in range(1, 11):
    print(i ** 3) 

# 10. Take input n, print numbers from 1 to n

n = int(input("Enter a number:-"))

for i in range(1, n+1):
    print(i)


# Section 2: While Loop

# 11. Print numbers from 1 to 20 using while

i = 1

while i <= 20:
    print(i)
    i += 1

# 12. Find factorial of a number using while

n = int(input("Enter a number:-"))

fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial=", fact)

# 13. Reverse a number using while

num = int(input("Enter the number:-"))

reverse = 0

while num != 0 :
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse number:-", reverse)

# 14. Count digits in a number

num = int(input("Enter a number:-"))

count =0

if num == 0:
    count = 1
else:
    while num != 0:
        num = num // 10
        count = count + 1
print("Number of digits:-", count)

# 15. Keep asking input until user enters "stop"

lst = []

while True:
    input1 = input("Enter the value:-")

    if input1 == "stop":
        break
    lst.append(input)

print(lst)


# Section 3: Nested Loop

# 16. Print pattern:
# *
# **
# ***
# ****

for i in range(1,5):
    print("*" * i)

# 17. Print pattern:
# 1
# 12
# 123
# 1234

for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end="")
    print()

# 18. Print multiplication table (1 to 5) using nested loop

for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")

    print()

# 19. Print:
# A B C
# A B C
# A B C

for i in range(3):
    for j in range(3):
        print(chr(65 + j), end=" " )

    print()

# 20. Print:
# 1 2 3
# 4 5 6
# 7 8 9

num = 1

for i in range(3):
    for j in range(3): 
        print(num,end=" ")
        num = num + 1

    print()


# Section 4: String Basics

#21. Count total characters in a string

text = input("Enter a string:-")

count = len(text)
print("Total charecters:-", count)

#22. Count vowels in a string

text = input("Enter a string:-")
count = 0

for string in text:
    if string.lower() in "aeiou":
        count = count + 1

print("Number of vowels:-", count)

#23. Count consonants in a string

text = input("Enter a string:-")
count = 0

for string in text:
    if string.isalpha() and string.lower() not in "aeiou":
        count = count + 1

print("Number of constants:-", count)

#24. Reverse a string using loop

text = input("Enter a string:-")
rev =""

for string in text:
    rev = string + rev

print("Reverse string:", rev)

#25. Check if string is palindrome

text = input("Enter a string:-")

if text == text[::-1]:
    print("Palinrome")
else:
    print("Not Palinrome")


# Section 5: String Slicing

#26. Print first 5 characters of a string

text = input("Enter a string:-")
print("First 5 charecters:-", text[:5])

#27. Print last 3 characters

text = input("Enter a string:-")
print("Last 3 charecters:-", text[-3:])

#28. Print string in reverse using slicing

text = input("Enter a string:-")
print("Reverese string:", text[::-1])

#29. Print every 2nd character

text = input("Enter a string: ")
print("Every 2nd character:", text[::2])

#30. Remove first and last character from string

text = input("Enter a string:-")
print("Result:", text[1: -1])


# Section 6: List Basics

#31. Create a list of 5 numbers and print sum

num = [1, 2, 3, 4, 5]
print("Sum:-",sum(num))

#32. Find maximum value in list

num = [1, 2, 3, 4, 5]
print("Max Value:", max(num))

#33. Find minimum value in list

num = [10, 25, 3, 40, 55]
print("Min Value:", min(num))

#34. Count total elements in list

num = [1, 2, 3, 4, 5]
print("Total Elements:", len(num))

#35. Check if element exists in list

numbers = [10, 20, 30, 40, 50]

num = int(input("Enter number:"))

if num in numbers:
    print("Element found")
else:
    print("Element not found")


#  Section 7: List Operations

# 36. Add 3 elements using append()

num = []
num.append(1)
num.append(2)
num.append(3)

print(num)

#37. Insert element at specific index

num = [ 10, 20, 30, 40]
num.insert(1, 15)

print(num)

#38. Remove element using remove()

num = [10, 20, 30, 40, 50]
num.remove(20)

print(num)

#39. Reverse list without using .reverse()

num = [10, 20, 30, 40, 50]
print("Reversed:", num[::-1])

#40. Sort list without using .sort()

cities = ["chennai", "bengaluru","hyderabad","pune"]

cities.sort()

print(cities)







