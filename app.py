from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        role = request.form.get("role")

        if email != "demo@gmail.com":
            error = "Wrong email"
        elif password != "1234":
            error = "Wrong password"
        else:
            if role == "student":
                return redirect(url_for("student_dashboard"))
            else:
                return redirect(url_for("mentor_dashboard"))

    return render_template("login.html", error=error)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/student")
def student_dashboard():
    return render_template("student_dashboard.html")

@app.route("/mentor")
def mentor_dashboard():
    return render_template("mentor_dashboard.html")
