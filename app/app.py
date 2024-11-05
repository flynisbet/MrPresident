from flask import Flask, jsonify, render_template, abort
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)

@app.route("/pres")
def presidentData():
    with open('../www/static/json/mrPresident.json', 'r') as file:
        presidents = json.load(file)
    return jsonify(presidents)

@app.route("/home")
def home(): 
    return render_template('index.html', page_title="Home_President")

@app.route("/about")
def about(): 
    return render_template('about.html', page_title = "About_Page")

@app.route("/game")
def quizGame():
    return render_template("quiz.html")

@app.route('/president/<int:president_number>')
def president_profile(president_number):
    with open('../www/static/json/mrPresident.json', 'r') as file:
        presidents = json.load(file)
    president = presidents.get(str(president_number))
    if not president:
        abort(404)
    return render_template('pres_profile.html', president=president)

@app.route("/")
def Hi():
    return render_template("quiz.html")



