import os
from flask import Flask, session, url_for, render_template, request

app = Flask(__name__)
app.secret_key = 'eoNio48tL934Nudbn98hfY'

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/drawpage")
def render_drawpage():
    return render_template('drawPage.html')

@app.route("/testpage")
def render_testpage():
    return render_template('testPage.html')

if __name__ == "__main__":
    app.run(debug=False, port=5001)
