from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hellow_world():
    return "Hellow World!"

from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

app.run(debug=True)