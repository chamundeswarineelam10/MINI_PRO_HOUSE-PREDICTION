import flask
from flask import Flask,render_template,request
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
with open('MINI_PRO_MODEL.pkl','rb') as f:
    c =pickle.load(f)

app = Flask(__name__)


@app.route('/')
def sample():
    return render_template('index.html')

@app.route("/predict",methods = ['GET','POST'])
def fun3():
    a = [float(i) for i in request.form.values()]
    b = [np.array(a)]
    predictions =c.predict(b)
    predictions =predictions[0]
    return render_template('index.html',prediction_text = predictions)


if __name__ == '__main__':
    app.run(debug=True)