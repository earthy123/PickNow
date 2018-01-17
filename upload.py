#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 16:37:20 2018

@author: earthz
"""

import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def upload_file():

    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)

