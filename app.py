from flask import Flask, request, make_response, flash, redirect, url_for, render_template, session
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import validators, SubmitField, TextField, FloatField, SelectField
import os
from utils import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfihhbgcuii82fer'
EFFICIENCY = [(0.16, 'Standard'), (0.25, 'Premium'), (0.11, 'Thin Layer')]
ARRAYTYPE = [(0, 'Fixed (Roof Top)'), (0, 'Fixed (Ground)'), (0.15, '1 - Axis Tracking'), (0.20, '2 - Axis Tracking')]

class CalculateForm(FlaskForm):
    area = FloatField('Area', validators=(validators.DataRequired(),))    
    modtype = SelectField('Module Type', choices=EFFICIENCY, validators=(validators.DataRequired(),))
    arrtype = SelectField('Array Type', choices=ARRAYTYPE, validators=(validators.DataRequired(),))
    tilt = FloatField('Tilt', validators=(validators.DataRequired(),))
    bill = FloatField('Current Electricity Bill', validators=(validators.DataRequired(),))
    submit = SubmitField('Calculate')

@app.route('/')
@app.route("/home")
def home():
    return render_template('index.html', title='SOLAR FOR INDIA')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    form = CalculateForm()
    if request.method=='POST':
        return redirect(url_for('results', area = request.form['area'], efficiency = request.form['modtype'], 
                                    extra = request.form['arrtype'], tilt = request.form['tilt'], bill = request.form['bill']))
    return render_template('calculator.html', title='Solar Calculator', form=form)

@app.route('/results', methods=['GET', 'POST'])
def results():
    
    area=float(request.args.get('area')), 
    efficiency=float(request.args.get('efficiency'))
    extra=float(request.args.get('extra'))
    tilt=float(request.args.get('tilt'))
    bill=float(request.args.get('bill'))
    LATITUDE = 10.8505

    try:
        os.remove('static/pictures/output_1.png')
    except:
        pass
    try:
        os.remove('static/pictures/output_2.png')
    except:
        pass

    if efficiency == 0.25:
        panelYield = 0.85
    elif efficiency == 0.16:
        panelYield = 0.8
    else:
        panelYield = 0.75

    energyOutputList = np.zeros(365)
    for day in range(1, 366):
        energyOutputList[day-1] = calcActualOutput(calcEnergyOutput(area, efficiency, 'Kerala', float(panelYield)), calcAzimuth(LATITUDE, day), tilt)
    energyOutputList = energyOutputList + extra * energyOutputList   
    avgEnergyOutput = float(np.mean(energyOutputList))

    
    if efficiency == 0.25:
        costOfInstall = 3500 * avgEnergyOutput * area[0]
    elif efficiency == 0.16:
        costOfInstall = 2000 * avgEnergyOutput * area[0] 
    else:
        costOfInstall = 3500 * avgEnergyOutput * area[0]
    costOfInstall = float(costOfInstall + extra * costOfInstall)
    
    returnEnergyPlot(area[0], efficiency, panelYield)
    crosspoint = returnPlot2(costOfInstall, float(bill), 0.1)

    print(costOfInstall)
    return render_template('results.html', title = 'Results', year=crosspoint)

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(debug=True)