from flask import Flask
# -*- coding: utf-8 -*-
from flask import request, render_template
import json

app = Flask(__name__)

@app.route('/')
def indexPage():
    return render_template('index.html')

@app.route('/dummy/streamer')
def DummyStreamerDataGet():
    f = open('dummysData.json', 'r')
    jsonData = json.load(f)
    f.close()
    return json.dumps(jsonData)

@app.route('/stream')
def StreamDataGet():
    return "Hello"

def main():
    app.debug = True
    app.run()


if __name__ == '__main__':
    main()
