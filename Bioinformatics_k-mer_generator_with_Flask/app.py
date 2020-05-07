#importing libraries
from flask import Flask, render_template, request

#creating instance of the class
app = Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/', methods = ['GET'])

def index():
    return render_template('main.html')


if __name__ == '__main__':
	app.run(debug=True)