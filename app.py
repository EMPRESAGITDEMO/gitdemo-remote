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

#Cálculo de edad
@app.route("/bd")
def age():
	return render_template("ageindex.html")

@app.route("/age", methods=['POST', 'GET'])
def agecalc():
	today = date.today()
	bd = request.form['date_input']
	birthday = datetime.strptime(bd, '%Y-%m-%d')
	age = today.year - birthday.year
	#age -= ((today.month, today.day) < (birthday.month, birthday.day))
	flash("Tu edad es: " + str(age) + " años")
	return render_template("ageindex2.html")

#Cálculo de índice de masa corporal
@app.route("/imc")
def sum():
	return render_template("imcindex.html")

@app.route("/sum", methods=['POST','GET'])
def sumcalc():
	peso = request.form['n1_input']
	estatura = request.form['n2_input']
	imc = round((float(peso)) / (((float(estatura))/100)**2),2)
	flash("Tu Índice de Masa Corporal (IMC) es: " + str(imc))
	return render_template("imcindex2.html")

HOST = "localhost"
PORT = 4000
DEBUG = True

if __name__ == '__main__':
	app.run(HOST, PORT, DEBUG)
