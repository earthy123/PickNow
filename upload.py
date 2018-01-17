#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
from flask import Flask, request, redirect, url_for, render_template
import sys
from werkzeug.utils import secure_filename
import requests

UPLOAD_FOLDER = './img/'
url = 'http://0.0.0.0:5000/'
a=UPLOAD_FOLDER+'matthias-clamer.jpeg'



app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def ss():
    return "Heyyy"

if __name__ == '__main__':
    app.run(debug=True)

