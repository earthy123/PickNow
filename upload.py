#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 16:37:20 2018

@author: earthz
"""
import requests
import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
import time
import sys
import base64
url = 'http://52.168.73.191:5000/'
UPLOAD_FOLDER = './img/'
CUTBG_FOLDER =  './bgimg/'
IMG64_FOLDER =  './img64/'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CUTBG_FOLDER'] = CUTBG_FOLDER


@app.route('/')
def index():
    return render_template("index.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def api(filename,filetype):
    try:
        files = {filetype: open(UPLOAD_FOLDER+filename, 'rb')}
        requests.post(url, files=files)
    except:
        pass

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST' and  'file' in request.files:
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            api(filename,'file')
    elif request.method == 'POST' and  'file_bg' in request.files:
        file = request.files['file_bg']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['CUTBG_FOLDER'], filename))
            

    return render_template('index2.html', image_name=filename)
@app.route('/base64', methods=['POST'])
def base6():
    if request.method == "POST":
        request_json = request.get_json()
        fileExt = request_json['number']
        imgbase64 = request_json['value']
        imgbase64= str.encode(imgbase64)
        timestr = time.strftime("%Y%m%d-%H%M%S")
#        print(imgbase64, file=sys.stderr)
        filename =timestr+'_base64'+'.'+fileExt
        with open(IMG64_FOLDER+filename, "wb") as fh:
            fh.write(base64.decodebytes(imgbase64))
#        api(filename,'file_base64')
        
    return 'OK'

@app.route('/upload/<filename>')
def receive_image(filename):
    original_img=filename
    name = original_img.rsplit('.', 1)[0]
    imageBg =name+'.png'
            # api(filename)
    return send_from_directory("bgimg",imageBg)

# @app.route('')


if __name__ == '__main__':
    app.run(debug=True)
