import sqlite3
import time

conn = sqlite3.connect('./static/menu.db', check_same_thread=False)
c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS menu (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                meal TEXT,
                timestamp REAL
    )""")

def add_meal(food):
    with conn:
        c.execute("INSERT INTO menu VALUES (?, ?, ?)", (None, food, time.time()))

def remove_meal(food):
    with conn:
        c.execute("DELETE FROM menu WHERE meal = ?", (food,))

def return_list_of_all_meals():
    c.execute("SELECT meal FROM menu ORDER BY timestamp DESC")
    meals = c.fetchall()
    mealList = [str(i[0]) for i in meals]
    return mealList




