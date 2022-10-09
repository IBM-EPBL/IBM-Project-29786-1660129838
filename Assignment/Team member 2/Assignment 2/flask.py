from flask import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')


if __name__ == '__main__':
    app.run(debug=True)