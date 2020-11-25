from flask import Flask, request, render_template
import pickle
import numpy as np
import re
import pandas as pd

app = Flask(__name__)

with open('models/nb_model.pkl', 'rb') as fopen:
    multinomial = pickle.load(fopen)

with open('models/vectorizer.pkl', 'rb') as fopen:
    vectorizer = pickle.load(fopen)


def text_preprocessing(string):
    string = re.sub('[^A-Za-z ]+', ' ', string)
    string = re.sub(r'[ ]+', ' ', string).strip()
    return string.lower()


@app.route('/', methods = ['GET'])
def hello():
    return render_template('index.html')


@app.route('/sentiment', methods = ['GET'])
def sentiment():
    text = text_preprocessing(request.args.get('text'))
    v = vectorizer.transform([text])
    return str(multinomial.predict(v)[0])

if __name__ == '__main__':
	app.run(debug=True)
