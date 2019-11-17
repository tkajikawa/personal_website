from flask import render_template, request, url_for, redirect, send_file
from app import app

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/spotify_api/')
def spotify_api():
    return render_template('chixtape.html')

@app.route('/more/')
def more():
    return render_template('more.html')