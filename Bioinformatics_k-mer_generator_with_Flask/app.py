import os
#importing libraries
from flask import Flask, request, render_template, send_from_directory


#creating instance of the class
app = Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/', methods = ['GET'])
def index():
    return render_template('main.html')

@app.route('/file-downloads', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        return render_template('generate.html', name = f.filename) 


if __name__ == '__main__':
	app.run(debug=True)