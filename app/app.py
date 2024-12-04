from flask import Flask, jsonify, render_template, abort
from flask_cors import CORS
import sqlite3
import json

app = Flask(__name__)
cors = CORS(app)

DATABASE = 'database.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/rank')
def ranking():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM President')
        users = cursor.fetchall()
    return render_template('ranking.html', page_title = "Ranking", presidents = users)

@app.route("/pres")
def presidentData():
    with open('../www/static/json/mrPresident.json', 'r') as file:
        presidents = json.load(file)
    return jsonify(presidents)

@app.route("/preQuiz")
def presidentQuiz():
    with open('../www/static/json/mrPresidentQuiz.json', 'r') as file:
        presidentQuiz = json.load(file)
    return jsonify(presidentQuiz)

@app.route("/timeline")
def timeline(): 
    return render_template('timeline.html', page_title="Home_President")

@app.route("/about")
def about(): 
    return render_template('about.html', page_title = "About_Page")

@app.route("/game/1")
def quizGame():
    return render_template("game/quiz_game.html")

@app.route('/president/<int:president_number>')
def president_profile(president_number):
    with open('../www/static/json/mrPresident.json', 'r') as file:
        presidents = json.load(file)
    president = presidents.get(str(president_number))
    
    if not president:
        abort(404)
    return render_template('pres_profile.html', president=president)

@app.route("/game")
def Hi():
    return render_template("game/game.html")

@app.route("/game/2")
def game2():
    return render_template("game/guess_game.html")


@app.route("/")
def homepage(): 
    return render_template("home.html")

