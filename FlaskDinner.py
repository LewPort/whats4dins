from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def theform():
    print('arse')
    return render_template('index.html')

@app.route('/name.html', methods=['POST'])
def butts():
    name = request.form['name']
    revname = name[::-1].title()
    namecount = str(len(name))
    fagname = alternatecaps(name)
    compliment = alternatecaps(random.choice(compliments))
    return render_template('name.html', name = name, revname=revname, namecount=namecount, fagname=fagname, compliment=compliment)

def alternatecaps(word):
    alternated = ''
    for i in range(len(word)):
        if (i % 2) == 0:
            alternated += word[i].upper()
        else:
            alternated += word[i].lower()
    return alternated

compliments = ['strong but sensitive individual xoxo', 'very smart and independent person xx', 'strong, independent black woman xxx']
            
        
if __name__ == '__main__':
    app.run(debug=True)
