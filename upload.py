#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 12:16:31 2018

@author: earthz
"""

from werkzeug.utils import secure_filename
import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory,send_file

url = 'http://13.92.130.243:5000'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def api(filename):
    files = {'file': open(filename, 'rb')}
    requests.post(url, files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            api(filename)
    return render_template('index2.html', image_name=filename)

@app.route('/finish')
def send_image(filename):
        if request.method == 'POST':
            
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
    #            print(filename, file=sys.stderr)
                file.save(os.path.join(app.config['CUTBG_FOLDER'], filename))
        return send_file('./cgb/'+filename)

# @app.route('')

if __name__ == '__main__':
    app.run(debug=True)
    app.run(port='5000')

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
if __name__ == '__main__':
    app.run(debug=True,port=5000)
#	app.run(debug=True)