#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
from flask import Flask, request, redirect, url_for, render_template,send_from_directory
import requests
from werkzeug.utils import secure_filename



url = 'http://52.168.73.191:5000/'


    
UPLOAD_FOLDER = './img/'
BG_FOLDER = './bgimg/'
app = Flask(__name__)
app.config['BG_FOLDER'] = BG_FOLDER
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg'])

def api(filename):
    try:
        files = {'file': open(UPLOAD_FOLDER+filename, 'rb')}
        requests.post(url, files=files)
    except:
        pass
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST' and 'file' in request.files:
            file=request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                api(filename)

    elif request.method == 'POST' and 'file_bg' in request.files:
            file=request.files['file_bg']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['BG_FOLDER'], filename))
    

    return render_template('index2.html')

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("bgimg",filename)

if __name__ == '__main__':
    app.run(debug=True)