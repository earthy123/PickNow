#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 12:16:31 2018

@author: earthz
"""

from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES

filename=""
app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'img'
configure_uploads(app, photos)

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return (filename)
        


#    return render_template('index.html')
    return render_template('index.html')
#    return render_template('index.html')

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
if __name__ == '__main__':
    app.run(debug=True,port=5000)
#	app.run(debug=True)
