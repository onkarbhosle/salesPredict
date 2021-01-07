from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('AdvertiseEfficiency.pickle', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        TV	=float(request.form['TV'])
        newspaper	=float(request.form['newspaper'])
        radio	=float(request.form['radio'])

        prediction=model.predict([[TV,newspaper,radio]])


        return render_template('home.html',prediction_text="sales prediction {}".format(prediction))
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

