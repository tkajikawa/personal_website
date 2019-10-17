from flask import render_template
from app import app

@app.route("/")
@app.route('/index/')
def home():
    return render_template('index.html')

@app.route('/aboutme/')
def aboutme():
    return render_template('aboutme.html')

@app.route('/music/')
def music():
    return render_template('music.html')