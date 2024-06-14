import numpy as np 
import pickle 
import joblib 
import matplotlib
import matplotlib. pyplot as plt 
import time 
import pandas 
import os
from flask import Flask, request, jsonify, render_template
from sklearn.preprocessing import scale
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
scale = pickle.load(open('encoder.pkl', 'rb'))
@app.route('/')

def home():
    return render_template ('index.html') #rendering the home page
 
@app.route('/predict',methods=[ "POST", "GET"])# route to show the predictions in a web UI def predict):


def predict():
  input_feature=[float(x) for x in request.form.values() ] 
  features_values=[np.array(input_feature)]
  names = [ 'holiday', 'temp','rain','snow', 'weather', 'day', 'month', 'year','hours','minutes', 'seconds']
  data = pandas.DataFrame(features_values, columns=names)
  data = scale.transform(data)
  data = pandas.DataFrame(data, columns = names)
# predictions using the loaded
  prediction =model.predict(data)
  print (prediction)
  text = "Estimated Traffic Volume is :"
  return render_template("index.html",prediction_text = text + str(prediction))

if __name__=="__main__":
# showing the prediction results in a UI
 port=int(os.environ.get('PORT',5000))
# running the app
app.run(debug=True, use_reloader=False)