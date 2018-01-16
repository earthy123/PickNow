#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 16:37:20 2018
 
@author: earthz
"""
import requests
import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import sys
UPLOAD_FOLDER = 'img'
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg'])
url = 'http://52.168.49.231:5000/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
def api(filename):
    files = {'file': open(filename, 'rb')}
    requests.post(url, files=files)
           
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
#            print(filename, file=sys.stderr)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#            api(filename)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0',port='5000')