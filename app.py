from flask import Flask, render_template, request, flash
from datetime import date, datetime
import webbrowser

from flask.wrappers import Request

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

#Saludo
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Hola " + str(request.form['name_input']) + " !")
	return render_template("index2.html")

HOST = "localhost"
PORT = 4000
DEBUG = True

if __name__ == '__main__':
	app.run(HOST, PORT, DEBUG)
