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

filename = "api/pkl_objets/model.pickle"
model = pickle.load(open(filename, 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
def result():

    name = request.form.get("name")
    age = int(request.form.get("age"))
    gender = int(request.form.get("gender"))
    height = int(request.form.get("height"))
    weight = int(request.form.get("weight"))
    ap_hi = int(request.form.get("ap_hi"))
    ap_lo = int(request.form.get("ap_lo"))
    cholesterol= int(request.form.get("cholesterol"))
    glucose = int(request.form.get("glucose"))
    smoke = int(request.form.get("smoke"))
    alcohol = int(request.form.get("alcohol"))
    activity = int(request.form.get("activity"))

    person = [[age*365.25, gender, height, weight, ap_hi, ap_lo, 
            cholesterol, glucose, smoke, alcohol, activity]]

    pred = model.predict(person)
    proba = model.predict_proba(person)

    return render_template('result.html', name = name, pred=pred, proba=round(proba[0, 1],3))

if __name__ == "__main__":
    app.run()
    

    