from datetime import date

class Transaction:
    def __init__(self, type, category, amount, description, date, is_recurring=False):
        self.type = type
        self.amount = amount
        self.description = description
        self.date = date
        self.is_recurring = is_recurring

    def __repr__(self):
        return f"[{self.date}] {self.type.upper()} | {self.category} | ${self.amount:.2f} | {self.description}"
    

    class SavingsGoal:
        def __init__(self, name, target_amount, saved_amount=0, deadline=None):
            self.name = name
            self.target_amount = target_amount
            self.saved_amount = saved_amount
            self.deadline = deadline

        def progress_percentage(self):
            return (self.saved_amount / self.target_amount) * 100
        
        def remaining(self):
            return self.target_amount - self.saved_amount
        
        def __repr__(self):
            return f"{self.name} | ${self.saved_amount:.2f} / ${self.target_amount:.2f} ({self.progress_percentage():.1f}%)"
            


class SavingsGoal:
    def __init__(self, name, target_amount, saved_amount=0, deadline=None):
        self.name = name
        self.target_amount = target_amount
        self.saved_amount = saved_amount
        self.deadline = deadline

    def progress_percentage(self):
        return (self.saved_amount / self.target_amount) * 100

    def remaining(self):
        return self.target_amount - self.saved_amount

    def __repr__(self):
        return f"{self.name} | ${self.saved_amount:.2f} / ${self.target_amount:.2f} ({self.progress_percentage():.1f}%)"