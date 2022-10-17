from markupsafe import escape
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__,template_folder='templates')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/About.html")
def About():
    return render_template("About.html")

@app.route("/login.html")
def login():
    return render_template("login.html")

@app.route("/signup.html")
def signup():
    return render_template("signup.html")    

if __name__ == "__main__":
    app.run(debug=True)
