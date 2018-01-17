#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os
from flask import Flask, request, redirect, url_for, render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES
from werkzeug.utils import secure_filename
import sys

app = Flask(__name__)
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
#            print(filename, file=sys.stderr)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)

