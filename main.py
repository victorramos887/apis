from flask import Flask

app = Flask(__name__)

@app.route("/")
def hellow_world():
    return "Hellow World"

if __name__ == "__main__":

    app.debug = True
    app.run(host="0.0.0.0", port = 5000)