from database import get_connection
from models import Transaction, SavingsGoal
from datetime import date

def add_transaction(type, category, amount, description, is_recurring=False):
    conn = get_connection()
    cursor = conn.cursor()
    today = str(date.today())

    cursor.execute("""
        INSERT INTO transactions (type, category, amount, description, date, is_recurring)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (type, category, amount, description, today, int(is_recurring)))

    conn.commit()
    conn.close()
    print(f"{type.capitalize()} of ${amount:.2f} added.")

def get_all_transactions():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.close()

    transactions = []
    for row in rows:
        t = Transaction(
            type=row[1],
            category=row[2],
            amount=row[3],
            description=row[4],
            date=row[5],
            is_recurring=bool(row[6])
        )
        transactions.append(t)
    return transactions

def get_summary():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
    total_income = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
    total_expenses = cursor.fetchone()[0] or 0

    conn.close()

    balance = total_income - total_expenses
    return total_income, total_expenses, balance

def add_savings_goal(name, target_amount, deadline=None):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO savings_goals (name, target_amount, saved_amount, deadline)
        VALUES (?, ?, 0, ?)
    """, (name, target_amount, deadline))

    conn.commit()
    conn.close()
    print(f"Savings goal '{name}' added.")

def update_savings_goal(goal_id, amount):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE savings_goals SET saved_amount = saved_amount + ? WHERE id = ?
    """, (amount, goal_id))

    conn.commit()
    conn.close()
    print(f"Savings goal updated.")

def get_all_goals():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM savings_goals")
    rows = cursor.fetchall()
    conn.close()

    goals = []
    for row in rows:
        g = SavingsGoal(
            name=row[1],
            target_amount=row[2],
            saved_amount=row[3],
            deadline=row[4]
        )
        goals.append(g)
    return goals

def apply_recurring_transactions():
    conn = get_connection()
    cursor = conn.cursor()
    today = str(date.today())

    cursor.execute("SELECT * FROM transactions WHERE is_recurring = 1")
    rows = cursor.fetchall()

    for row in rows:
        cursor.execute("""
            INSERT INTO transactions (type, category, amount, description, date, is_recurring)
            VALUES (?, ?, ?, ?, ?, 0)
        """, (row[1], row[2], row[3], row[4], today))

    conn.commit()
    conn.close()
    print(f"{len(rows)} recurring transaction(s) applied.")