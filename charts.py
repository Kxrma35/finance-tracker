import matplotlib.pyplot as plt
from tracker import get_all_transactions

def plot_spending_by_category():
    transactions = get_all_transactions()
    expenses = [t for t in transactions if t.type == 'expense']

    if not expenses:
        print("No expenses to chart yet.")
        return
    
    categories = {}
    for t in expenses:
        categories[t.category] = categories.get(t.category, 0) + t.amount

    labels = list(categories.keys())
    values = list(categories.values())

    plt.figure(figsize=(7, 7))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("spending by Category")
    plt.tight__layout()
    plt.show()

def plot_income_vs_expenses():
    total_icome, total_expenses, balance = get_summary()

    labels = ['Income', 'Expenses']
    values = [total_income, total_expenses]
    colors = ['#2ecc71' '#e74c3c']

    plt.figure(figsize=(6, 5))
    bars = plt.bar(labels, values, color=colors)
    plt.title("Income vs Expenses")
    plt.ylabel("Amount ($)")

    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width() / 2,
                 bar.get_height() + 10,
                 f"${value:.2f}",
                 ha='center', fontsize=11)
        
    plt.tight_layout()
    plt.show()

def plot_savings_progress(goals):
    if not goals:
        print("NO savings to chart yet.")
        return
    names = [g.name for g in goals]
    saved = [g.saved_amount for g in goals]
    targets = [g.target_amount for g in goals]

    x = range(len(names))
    width = 0.35

    plt.figure(figsize=(8, 5))
    plt.bar([i - width/2 for i in x], saved, width, label='Saved', color='#3498db')
    plt.bar([i + width/2 for i in x], targets, width, label='Target', color='#95a5a6')

    plt.title("Savings Goals Progress")
    plt.ylabel("Amount ($)")
    plt.xticks(x, names)
    plt.legend()
    plt.tight_layout()
    plt.show()