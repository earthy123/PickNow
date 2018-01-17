#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hey its Python Flask application!'

app = Flask(__name__)

@app.route('/')
def upload_file():

    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)

