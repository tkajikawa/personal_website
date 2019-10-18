from flask import render_template, request, url_for, redirect
from app import app

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('aboutme.html'))
    return render_template('index.html')

@app.route('/aboutme/')
def aboutme():
    return render_template('aboutme.html')

@app.route('/music/')
def music():
    return render_template('music.html')