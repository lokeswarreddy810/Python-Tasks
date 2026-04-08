from abc import ABC, abstractmethod
from functools import reduce
from datetime import datetime

#Abstract Class
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


#User Class(Encapsulation)
class User(AbstractUser):
    def __init__(self, name, user_id):
        self.__name = name
        self.__user_id = user_id

    def get_details(self):
        return f"User: {self.__name}, ID: {self.__user_id}"
    
    def get_user_id(self):
        return self.__user_id
    
#Expense Class(Inheritence)
class Expense(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self.__expenses = []

    #Add Expense
    def add_expense(self, amount, category, description, date):
        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.strptime(date, "%Y-%m-%d")
        }
        self.__expenses.append(expense)

    #View Expenses
    def get_details(self):
        print(super().get_details())
        for exp in self.__expenses:
            print(exp)

    #Filter by Category
    def filter_by_category(self, category):
        return list(filter(lambda x: x["category"] == category, self.__expenses))
    
    #Filter by Date

    def filter_by_date(self, date):
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        return [exp for exp in self.__expenses if exp["date"] == date_obj]
    
    #Total Expense Using map + reduce 
    def total_expense(self):
        amounts = list(map(lambda x: x["amount"], self.__expenses))
        return reduce(lambda x, y: x+y, amounts, 0)
    
    #Category-wise Spending
    def category_wise(self):
        categories = set(exp["category"] for exp in self.__expenses)
        return{
            cat: sum(exp ["amount"] for exp in self.__expenses if exp["category"] == cat)
            for cat in categories
        }
    
    # Delete Expense
    def delete_expense(self, index):
        if 0 <= index < len(self.__expenses):
            self.__expenses.pop(index)
    
    #Update Expense
    def update_expense(self, index, amount=None, category = None):
        if 0 <= index < len(self.__expenses):
            if amount:
                self.__expenses[index]["amount"] = amount
            if category:
                self.__expenses[index]["category"] = category

    #Monthly Report
    def monthly_report(self):
        report = {}
        for exp in self.__expenses:
            month = exp["date"].strftime("%Y-%m")
            report[month] = report.get(month, 0) + exp["amount"]
        return report
    
    # Highest Expense using reduce
    def highest_expense(self):
        return reduce(
            lambda x, y: x if x["amount"] > y["amount"] else y,
            self.__expenses
        ) if self.__expenses else None

    # Smart Insight
    def smart_insight(self):
        category_data = self.category_wise()
        if not category_data:
            return "No data available"

        max_category = max(category_data, key=category_data.get)
        return f"You are spending too much on {max_category} this month!"
    

    
    

