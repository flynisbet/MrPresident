from flask import Flask, jsonify, render_template
from flask_cors import CORS
import json

app = Flask(__name__, template_folder="../www/templates")
cors = CORS(app)

@app.route("/pres")
def presidentData():
    with open('../www/static/json/mrPresident.json', 'r') as file:
        presidents = json.load(file)

@app.route("/")
def home():
    return render_template("index.html")