from database import initialize_db
from tracker import (add_transaction, get_all_transactions,
                     get_summary, add_savings_goal,
                     update_savings_goal, get_all_goals,
                     apply_recurring_transactions)
from charts import plot_spending_by_category, plot_income_vs_expenses, plot_savings_progress
from reports import generate_report

def print_menu():
    print("""
╔══════════════════════════════════╗
║        Personal Finance Tracker  ║
╠══════════════════════════════════╣
║  1. Add Income                   ║
║  2. Add Expense                  ║
║  3. View All Transactions        ║
║  4. View Summary                 ║
║  5. Add Savings Goal             ║
║  6. Update Savings Goal          ║
║  7. View Savings Goals           ║
║  8. Apply Recurring Transactions ║
║  9. View Charts                  ║
║  10. Export PDF Report           ║
║  0. Exit                         ║
╚══════════════════════════════════╝
    """)

def handle_add_transaction(type):
    category = input("Category (e.g. food, rent, salary): ").strip()
    amount = float(input("Amount: $"))
    description = input("Description (optional): ").strip()
    recurring = input("Is this recurring? (y/n): ").strip().lower() == 'y'
    add_transaction(type, category, amount, description, recurring)

def handle_view_transactions():
    transactions = get_all_transactions()
    if not transactions:
        print("No transactions yet.")
        return
    print()
    for t in transactions:
        print(t)

def handle_view_summary():
    income, expenses, balance = get_summary()
    print(f"""
  Summary
---------------------------
 Total Income:   ${income:.2f}
 Total Expenses: ${expenses:.2f}
 Balance:        ${balance:.2f}
    """)

def handle_add_goal():
    name = input("Goal name (e.g. Emergency Fund): ").strip()
    target = float(input("Target amount: $"))
    deadline = input("Deadline (YYYY-MM-DD) or press Enter to skip: ").strip() or None
    add_savings_goal(name, target, deadline)

def handle_update_goal():
    goals = get_all_goals()
    if not goals:
        print("No goals yet.")
        return
    for i, g in enumerate(goals, start=1):
        print(f"{i}. {g}")
    choice = int(input("Select goal number: ")) - 1
    amount = float(input("Amount to add: $"))
    update_savings_goal(choice + 1, amount)

def handle_view_goals():
    goals = get_all_goals()
    if not goals:
        print("No savings goals yet.")
        return
    print()
    for g in goals:
        print(g)

def handle_charts():
    print("""
 Charts
1. Spending by Category
2. Income vs Expenses
3. Savings Goals Progress
    """)
    choice = input("Choose a chart: ").strip()
    if choice == '1':
        plot_spending_by_category()
    elif choice == '2':
        plot_income_vs_expenses()
    elif choice == '3':
        plot_savings_progress(get_all_goals())
    else:
        print("Invalid choice.")

def main():
    initialize_db()
    
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            handle_add_transaction('income')
        elif choice == '2':
            handle_add_transaction('expense')
        elif choice == '3':
            handle_view_transactions()
        elif choice == '4':
            handle_view_summary()
        elif choice == '5':
            handle_add_goal()
        elif choice == '6':
            handle_update_goal()
        elif choice == '7':
            handle_view_goals()
        elif choice == '8':
            apply_recurring_transactions()
        elif choice == '9':
            handle_charts()
        elif choice == '10':
            generate_report()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()