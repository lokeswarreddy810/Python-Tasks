# Task 1: User Info Manager (Functions + Dictionary)

def create_user(name, age, role):
    user = {
        "name" : name.title(),
        "age" : age,
        "role" : role
            }
    
    return user

users = [
    create_user("Lokesh", 25, "Python Developer"),
    create_user("Sampath", 23, "HR"),
    create_user("Pradeep", 24, "Business Analyst")
]

print("All Users")
for user in users:
    print(f" Name:{user['name']}, Age:{user['age']}, Role:{user['role']}")


# Task 2: Dynamic Calculator (*args)

def calculate_total(*numbers):
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return total, average
    
result = calculate_total(10, 20, 30, 40, 50)
print("Total:", result[0])
print("Average:", result[1])


#  Task 3: Keyword Config System (**kwargs)

def system_config(**settings):
    for key, value in settings.items():
        print(f"{key} : {value}")

print("\nSystem Config:")
system_config(mode = "debug", version = "1.0")


#  Task 4: Factorial Service (Recursion)

def factorial(n):
    if n < 0:
        return "Error: Negative numbers not allowed for factorial"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print("\nFactorial Results:")
print(factorial(5))

# Task 5: Memory Optimization (Generator)

def square_generator(n):
    for i in range(n):
        yield i * i
    
gen = square_generator(5)

for num in gen:
    print(num)

normal_list = [i * i for i in range(5)]

print("List_type:", type(normal_list))
print("Generator type:", type(square_generator(5)))


# Task 6: Exception Handling Module

try:
    numerator = int(input("Enter numerator:"))
    denominator = int(input("Enter denominator:"))

    result = numerator / denominator
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input")

finally:
    print("Program completed")


#  Task 7: File Handling

file = open("team_data.txt", "w")

file.write("Lokesh, 25, Developer\n")
file.write("Sai, 22, Designer\n")

file.close()

file = open("team_data.txt", "r")

content = file.read()
print(content)

file.close()
print("Is file closed?", file.closed)