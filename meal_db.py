import psycopg2
import time
import sys
import os

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS menu (
                id SERIAL PRIMARY KEY,
                meal TEXT,
                timestamp NUMERIC
    )""")

def add_meal(food):
    with conn:
        c.execute("INSERT INTO menu (meal, timestamp) VALUES (%s, %s)", (food, time.time()))
    sys.stdout.write('Added %s to DB' % food)

def remove_meal(food):
    with conn:
        c.execute("DELETE FROM menu WHERE meal = %s", (food,))
    sys.stdout.write('Removed %s from DB' % food)

def return_list_of_all_meals():
    c.execute("SELECT meal FROM menu ORDER BY timestamp DESC")
    meals = c.fetchall()
    mealList = [str(i[0]) for i in meals]
    return mealList




