from flask import Flask, render_template, request, url_for, redirect
import meal_db
import random

app = Flask(__name__)

_MENU = []
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

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', pre=randitem(_PRE), food=randitem(_MENU).upper() + "?")

@app.route('/mgr', methods=['GET'])
def manager():
    return render_template('mgr.html', menu=_MENU)

@app.route('/add', methods=['GET', 'POST'])
def add():
    meal = request.form['mealname']
    meal_db.add_meal(meal)
    refresh_menu()
    return redirect(url_for('manager'))

@app.route('/remove', methods=['GET', 'POST'])
def remove():
    meal = request.form['mealtoremove']
    meal_db.remove_meal(meal)
    refresh_menu()
    return redirect(url_for('manager'))

def randitem(list):
    return random.choice(list)

def refresh_menu():
    global _MENU
    menu = meal_db.return_list_of_all_meals()
    _MENU = menu

meal_db.create_table()
refresh_menu()

if __name__ == '__main__':
    meal_db.create_table()
    refresh_menu()
    app.run(debug=True)