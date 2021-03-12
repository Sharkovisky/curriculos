from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/home')
def home():
    l = ['Programador front-end', 'Programador back-end', 'Devops']
    return render_template('index.html', lista=l)
