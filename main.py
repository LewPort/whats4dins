from flask import Flask, render_template, request, url_for, redirect
import meal_db
import random
import time
import sys

app = Flask(__name__)

_MENU = ['Falafel Wraps', 'Baked Potato & Beans', 'Banh Mi', 'Pasta Bake', 'Stir Fry', 'Nachos with guacamole!', 'EGGGGGGG SANDWICHHHHH', 'Summer Rolls', 'Soup', 'Roast Dinz', 'Pho', 'Bake a loaf', 'Quesodillas', 'Enchilladas! With quorn mince and baked beans and cheese and jalapenos etc', 'Brownies', "That fried burger 'meat' + grilled chilli sandwich that Mark Weins ate in Turkey", 'Dumplings', 'Fiorentina Pizza', 'Apple Pie', 'Macaroni Cheese', 'Lasagne', 'Avocado on Toast', 'Blowtorched-Cheese Topped Sushi', 'SUUUSHIIIIII!!!', 'Something Vietnamese', 'Egg fried rice', 'Indiannnnn', 'Hummous', 'Pizza', 'Bruschetta', 'Pesto Pasta', 'Hotdogs', 'Burgers', 'Burritos', 'Tacos', 'Makhani Curry', 'Nachos with guacamole!', 'EGGGGGGG SANDWICHHHHH', 'Summer Rolls', 'Soup', 'Roast Dinz', 'Pho', 'Bake a loaf', 'Quesodillas', 'Enchilladas! With quorn mince and baked beans and cheese and jalapenos etc', 'Brownies', "That fried burger 'meat' + grilled chilli sandwich that Mark Weins ate in Turkey", 'Dumplings', 'Fiorentina Pizza', 'Apple Pie', 'Macaroni Cheese', 'Lasagne', 'Avocado on Toast', 'Blowtorched-Cheese Topped Sushi', 'SUUUSHIIIIII!!!', 'Something Vietnamese', 'Egg fried rice', 'Indiannnnn', 'Hummous', 'Pizza', 'Bruschetta', 'Pesto Pasta', 'Hotdogs', 'Burgers', 'Burritos', 'Tacos', 'Makhani Curry']
_PRE = [
'How aboutttt...',
'Consider this:',
'What about...',
'Let\'s think about...',
'What about...',
'I fancy...',
'OMGGGG!!!!',
'I\'m in the mood for...',
'You\'re thinking about...',
'Let\'s haveeeee...',
'Tell you what sounds good...'
]

@app.route('/')
def index():
    return render_template('index.html', pre=randitem(_PRE), food=randitem(_MENU).upper() + "?")

@app.route('/mgr')
def manager():
    refresh_menu()
    return render_template('mgr.html', menu=_MENU)

@app.route('/add', methods=['POST'])
def add():
    meal = request.form.get('mealname', None)
    meal_db.add_meal(meal)
    refresh_menu()
    return redirect(url_for('manager'))

@app.route('/remove', methods=['POST'])
def remove():
    meal = request.form.get('mealtoremove', None)
    if meal:
        meal_db.remove_meal(meal)
        refresh_menu()
    return redirect(url_for('manager'))

def randitem(list):
    return random.choice(list)

def refresh_menu():
    global _MENU
    time.sleep(0.5)
    _MENU = meal_db.return_list_of_all_meals()
    sys.stdout.write('REFRESH MENU: Main.py _MENU list repopulated from the database.')

def populate_table_if_empty():
    global _MENU
    if not meal_db.return_list_of_all_meals():
        for i in _MENU:
            meal_db.add_meal(i)
    sys.stdout.write('Database was found to be blank, so was populated using the default list of foods.')
    _MENU = []

meal_db.create_table()
populate_table_if_empty()
refresh_menu()

if __name__ == '__main__':
    app.run(debug=True)