class PersonalFinanceAssistant:
    def __init__(self):
        self.income = 0.0
        self.expenses = []
        self.balance = 0.0
        self.budget = {}
        self.goals = {}
        self.investments = []

    def set_income(self, income):
        self.income = float(income)
        self.balance += self.income

    def add_expense(self, category, amount):
        expense = {
            'category': category,
            'amount': float(amount)
        }
        self.expenses.append(expense)
        self.balance -= expense['amount']

    def set_budget(self, category, amount):
        self.budget[category] = float(amount)

    def set_goal(self, goal, amount):
        self.goals[goal] = float(amount)

    def add_investment(self, investment):
        self.investments.append(investment)

    def analyze_expenses(self):
        analysis = {}
        for expense in self.expenses:
            category = expense['category']
            amount = expense['amount']
            if category not in analysis:
                analysis[category] = amount
            else:
                analysis[category] += amount
        return analysis

    def optimize_expenses(self):
        analysis = self.analyze_expenses()
        for category, amount in analysis.items():
            if amount > self.budget.get(category, 0.0):
                extra = amount - self.budget.get(category, 0.0)
                print(f"You exceeded the budget for {category} by {extra}.")

    def recommend_investment_strategy(self):
        # Use AI algorithm to propose investment strategies based on risk tolerance, goals, and market data
        pass

    def track_progress(self):
        for goal, amount in self.goals.items():
            if self.balance >= amount:
                print(f"Congratulations! You have achieved your {goal} goal.")
            else:
                remaining = amount - self.balance
                print(f"You need {remaining} more to achieve your {goal} goal.")

    def send_reminder(self, message):
        # Send personalized reminders to users for bill payments, investment opportunities, etc.
        pass

    def ensure_security_and_privacy(self):
        # Implement security and privacy measures for users' financial data
        pass

# Usage example:
assistant = PersonalFinanceAssistant()
assistant.set_income(5000)
assistant.add_expense('Rent', 1500)
assistant.add_expense('Food', 400)
assistant.set_budget('Food', 300)
assistant.optimize_expenses()
assistant.set_goal('Retirement', 100000)
assistant.track_progress()