# -*- coding: utf-8 -*-
"""flask_fish_analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ic7KvPiWWl9nO5nYGLcDg-bSHkD11U0g
"""

from flask import Flask, render_template, request
import pickle
import  os
import pandas as pd

app = Flask(__name__,template_folder="Template",static_folder="Template")
filename = 'Fish_LR.sav'
fish_model = pickle.load(open(filename, 'rb'))
port = int(os.environ.get("PORT", 8000))

@app.route('/')
def index():
    return render_template(r'new.html')

@app.route('/pred', methods=['POST'])
def pred():
    print(dict(request.form))
    # form = request.form.values()
    # vals = [float(i) for i in list(form)]
    df = pd.DataFrame(dict(request.form),index=[0])
    print(df)
    df.columns = ['Weight', 'Length1', 'Length2', 'Length3', 'Height', 'Width']
    print(df)
    predictedvalue= fish_model.predict(df)
    Species={1:'Bream',2:'Roach',3:'Whitefish', 4:'Parkki',5:'Perch',6:'Pike',7:'Smelt'}
    prediction=Species.get(predictedvalue[0])
    print(prediction)
    return render_template(r'new.html', prediction_text='The predicted fish Species is: {}'.format(prediction))

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port=port)