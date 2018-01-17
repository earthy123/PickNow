#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
from flask import Flask, request, redirect, url_for, render_template

from werkzeug.utils import secure_filename
import requests

UPLOAD_FOLDER = './img/'
url = 'http://52.168.73.191:5000/'
a=UPLOAD_FOLDER+'matthias-clamer.jpeg'
def api(filename):
    files = {'file': open(UPLOAD_FOLDER+filename, 'rb')}
    requests.post(url, files=files)
    

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def ss():
    api(a)
    
    return "Hi"
if __name__ == '__main__':
    app.run(debug=True)

