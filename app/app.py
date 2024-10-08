from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/pres")
def presidentData():
    presidents = [{
      "name": "Joe Biden",
      "president_number": 46,
      "picture_link": "../static/img/46_Biden.jpeg",
      "serving_years": "2021-present",
      "description": "Joe Biden, the 46th president of the United States, previously served as Vice President under Barack Obama and as a long-time U.S. Senator from Delaware."
    },
    {
      "name": "Donald Trump",
      "president_number": 45,
      "picture_link": "../static/img/45_Trump.jpeg",
      "serving_years": "2017-2021",
      "description": "Donald Trump, a businessman and television personality, was the 45th president, known for his 'America First' policy and unconventional approach to governance."
    },
    {
      "name": "Barack Obama",
      "president_number": 44,
      "picture_link": "../static/img/44_Obama.jpeg",
      "serving_years": "2009-2017",
      "description": "Barack Obama was the first African American president of the United States, serving two terms. He is known for healthcare reform and the killing of Osama bin Laden."
    },
    {
      "name": "George W. Bush",
      "president_number": 43,
      "picture_link": "../static/img/46_Biden.jpeg",
      "serving_years": "2001-2009",
      "description": "George W. Bush served as president during the 9/11 attacks and initiated the wars in Afghanistan and Iraq. He also implemented tax cuts and education reform."
    },
    {
      "name": "Bill Clinton",
      "president_number": 42,
      "picture_link": "../static/img/46_Biden.jpeg",
      "serving_years": "1993-2001",
      "description": "Bill Clinton served two terms during a period of economic prosperity and led initiatives on healthcare reform, education, and welfare."
    },
    {
      "name": "George H. W. Bush",
      "president_number": 41,
      "picture_link": "../static/img/46_Biden.jpeg",
      "serving_years": "1989-1993",
      "description": "George H. W. Bush led the U.S. through the end of the Cold War and the Gulf War, emphasizing diplomacy and a 'kinder, gentler nation.'"
    },
    {
      "name": "Ronald Reagan",
      "president_number": 40,
      "picture_link": "../static/img/46_Biden.jpeg",
      "serving_years": "1981-1989",
      "description": "Ronald Reagan, a former actor and governor of California, is remembered for his role in ending the Cold War and promoting conservative economic policies."
    },
    {
      "name": "Jimmy Carter",
      "president_number": 39,
      "picture_link": "../static/img/46_Biden.jpeg",
      "serving_years": "1977-1981",
      "description": "Jimmy Carter, a former governor of Georgia, focused on human rights and diplomacy. He was awarded the Nobel Peace Prize in 2002 for his post-presidency humanitarian work."
    },
    {
      "name": "Gerald Ford",
      "president_number": 38,
      "picture_link": "../static/img/46_Biden.jpeg",
      "serving_years": "1974-1977",
      "description": "Gerald Ford assumed the presidency following Nixon's resignation. He is known for pardoning Nixon and overseeing a troubled economy."
    },
    {
      "name": "Richard Nixon",
      "president_number": 37,
      "picture_link": "../static/img/46_Biden.jpeg",
      "serving_years": "1969-1974",
      "description": "Richard Nixon is remembered for his foreign policy achievements, including opening relations with China, but resigned after the Watergate scandal."
    }]

    return jsonify(presidents)