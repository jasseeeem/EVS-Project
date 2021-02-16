from flask import Flask, request, flash, redirect, url_for, render_template, session
# from flask_wtf import FlaskForm
# from wtforms.fields.html5 import DateField
# from wtforms.validators import DataRequired
# from wtforms import validators, SubmitField, TextField
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
from flask_googlemaps import GoogleMaps, Map

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SECRET_KEY'] = 'dfihhbgcuii82fer'
# db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def mapview():
    return render_template('index.html', title='Solar Calculator')

# @app.route('/calculate', methods=['GET', 'POST'])
# def calculate():

if __name__ == "__main__":
    app.run(debug=True)