from flask import Flask, jsonify, render_template
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


