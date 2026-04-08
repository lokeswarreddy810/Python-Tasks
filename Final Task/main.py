from User import Expense
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",   
    database="expense_db"
)

cursor = conn.cursor()

# Create User
name = input("Enter user name: ")

cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
conn.commit()

user_id = cursor.lastrowid   
user = Expense(name, user_id)

print(f" User created with ID: {user_id}")

# MENU 
while True:
    print("\n====== SMART EXPENSE MANAGER ======")
    print("1. Add Expense")
    print("2. View Expenses (JOIN)")
    print("3. Filter by Category")
    print("4. Filter by Date")
    print("5. Total Expense")
    print("6. Category-wise Spending")
    print("7. Monthly Report")
    print("8. Highest Expense")
    print("9. Smart Insight")
    print("10. Update Expense (SQL)")
    print("11. Delete Expense (SQL)")
    print("0. Exit")

    choice = int(input("Enter choice: "))

    # 1. Add Expense
    if choice == 1:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")
        date = input("Enter date (YYYY-MM-DD): ")

        user.add_expense(amount, category, description, date)

        query = """
        INSERT INTO expenses (user_id, amount, category, description, date)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (user_id, amount, category, description, date))
        conn.commit()

        print(" Expense Added")

    # 2. View Expenses (JOIN)
    elif choice == 2:
        print("\n Expenses from Database:")

        query = """
        SELECT u.name, e.exp_id, e.amount, e.category, e.description, e.date
        FROM users u
        JOIN expenses e ON u.user_id = e.user_id
        WHERE u.user_id = %s
        """
        cursor.execute(query, (user_id,))

        for row in cursor.fetchall():
            print(row)

    # 3. Filter by Category 
    elif choice == 3:
        cat = input("Enter category: ")
        print(user.filter_by_category(cat))

    # 4. Filter by Date 
    elif choice == 4:
        date = input("Enter date (YYYY-MM-DD): ")
        print(user.filter_by_date(date))

    # 5. Total Expense
    elif choice == 5:
        print("Total:", user.total_expense())

    # 6. Category-wise
    elif choice == 6:
        print(user.category_wise())

    # 7. Monthly Report
    elif choice == 7:
        print(user.monthly_report())

    # 8. Highest Expense
    elif choice == 8:
        print(user.highest_expense())

    # 9. Smart Insight
    elif choice == 9:
        print(user.smart_insight())

    # 10. Update Expense 
    elif choice == 10:
        exp_id = int(input("Enter expense ID: "))
        new_amount = float(input("Enter new amount: "))

        cursor.execute(
            "UPDATE expenses SET amount=%s WHERE exp_id=%s",
            (new_amount, exp_id)
        )
        conn.commit()

        print("Expense Updated in DB")

    # 11. Delete Expense 
    elif choice == 11:
        exp_id = int(input("Enter expense ID: "))

        cursor.execute(
            "DELETE FROM expenses WHERE exp_id=%s",
            (exp_id,)
        )
        conn.commit()

        print(" Expense Deleted from DB")

    # Exit
    elif choice == 0:
        print("Exiting...")
        break

    else:
        print(" Invalid choice")

cursor.close()
conn.close()





