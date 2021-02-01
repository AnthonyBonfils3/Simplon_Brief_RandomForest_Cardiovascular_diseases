#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Fev 01 13:11:37 2021

@author: Bonfils
"""

from flask import Flask, render_template, url_for, request
import pandas as pd
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
def result():
    filename = "models/model.pickle"
    model = pickle.load(open(filename, 'rb'))

    name = request.form.get("name")
    age = request.form.get("age")*365.25
    gender = request.form.get("gender")
    height = request.form.get("height")
    weight = request.form.get("weight")
    ap_hi = request.form.get("ap_hi")
    ap_lo = request.form.get("ap_lo")
    cholesterol= request.form.get("cholesterol")
    glucose = request.form.get("glucose")
    smoke = request.form.get("smoke")
    alcohol = request.form.get("alcohol")
    activity = request.form.get("activity")

    person = [[age, gender, height, weight, ap_hi, ap_lo, 
            cholesterol, glucose, smoke, alcohol, activity]]

    pred = model.predict(person)
    proba = model.predict_proba(person)

    return render_template('result.html', name = name, pred=pred[0, 1].round(3), proba=proba)

if __name__ == "__main__":
    app.run()
    

    