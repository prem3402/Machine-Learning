from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def welcome():
    return "<h1>This is homepage for flask app"


@app.route("/index")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
