from flask import render_template, request, redirect
from app import app
from models.events import events, add_new_event
from models.event import *

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods=['POST'])
def add_event():
    date = request.form['date']
    name = request.form['name']
    guests = request.form['guests']
    room = request.form['room']
    description = request.form["description"]
    #return redirect('/events')
    return render_template('index.html', title='Home', events=events)
    



