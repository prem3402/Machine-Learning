from flask import Flask


# creating instance of Flask
app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to Flask App"


@app.route("/index")
def index():
    return "Welcome to Index Page"


if __name__ == "__main__":
    app.run(debug=True)
