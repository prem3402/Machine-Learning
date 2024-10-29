from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def homepage():
    return "<h1>Home Page</h1>"


@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")


# @app.route("/form", methods=["GET", "POST"])
# def form():
#     if request.method == "POST":
#         name = request.form["name"]
#         return f"Hello {name}!"
#     return render_template("form.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello {name}!"
    return render_template("form.html")


@app.route("/success/<int:num>")
def success(num):
    res = ""
    if num >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    exp = {"score": num, "res": res}
    return render_template("result1.html", results=exp)


@app.route("/successif/<int:num>")
def successif(num):
    return render_template("result2.html", results=num)


if __name__ == "__main__":
    app.run(debug=True)
