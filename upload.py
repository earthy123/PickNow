#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES




app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():

    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)

