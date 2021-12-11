from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        year = int(request.form['year'])
        original_price=float(request.form['original_price'])
        mileage=int(request.form['mileage'])
        owners=int(request.form['owners'])
        accidents=int(request.form['accidents'])
        age= int(2021 - year)
        X_test = [year,mileage,accidents,owners,age,original_price]
        
        prediction= model.predict([[year,mileage,accidents,owners,age,original_price    ]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_text="Car cannot be sold")
        else:
            return render_template('index.html',prediction_text="Car's predicted value is ${}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
