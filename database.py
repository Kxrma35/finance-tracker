import sqlite3

DB_NAME = "finance.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              type TEXT NOT NULL,
              category TEXT NOT NULL, 
              amount REAL NOT NULL,
              description TEXT,
              date TEXT NOT NULL,
              is_recurring INTEGER DEFAULT 0         
         )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS savings_goals (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             target_amount REAL NOT NULL,
             saved_amount REAL DEFAULT 0,
             deadline TEXT
                   
        )
    """)

    conn.commit()
    conn.close()
    print("Database initialized")
    
