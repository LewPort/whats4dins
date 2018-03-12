import psycopg2
import time
import os

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS menu (
                id SERIAL PRIMARY KEY,
                meal TEXT,
                timestamp REAL
    )""")

def add_meal(food):
    with conn:
        c.execute("INSERT INTO menu VALUES (%s, %s, %s)", (None, food, time.time()))

def remove_meal(food):
    with conn:
        c.execute("DELETE FROM menu WHERE meal = %s", (food,))

def return_list_of_all_meals():
    c.execute("SELECT meal FROM menu ORDER BY timestamp DESC")
    meals = c.fetchall()
    mealList = [str(i[0]) for i in meals]
    return mealList




