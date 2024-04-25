# app.py
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"

#set FLASK_APP=D:\git-anhanguera\poc\flask\hello-world.py
#set FLASK_ENV=development
#flask run
#python -m flask run