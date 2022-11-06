from distutils.log import debug
from flask import Flask, render_template, url_for

app = Flask(__name__,static_url_path='/static')

@app.route('/')
def home():
    return render_template("home_body.html")

@app.route('/login')
def sign_in():
    return render_template("sign_in.html")

@app.route('/signup')
def sign_up():
    return render_template("sign_up.html")
if __name__ == '__main__':
    app.run(debug=True)