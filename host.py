from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lander.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/physician-login')
def software():
    return render_template('phylogin.html')

@app.route('/aboutus')
def dashboard():
    return render_template('ptdash.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80) 