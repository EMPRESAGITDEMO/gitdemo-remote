from flask import Flask, render_template, request, flash
from datetime import date, datetime
import webbrowser

from flask.wrappers import Request

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

HOST = "localhost"
PORT = 4000
DEBUG = True

if __name__ == '__main__':
	app.run(HOST, PORT, DEBUG)
