#!/usr/bin/python3

from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', defaults={'path': '/'})
@app.route('/<path:path>', methods=["POST", "GET"])
def receive(path) :
    return "HelloWorld"

app.debug = True
app.run(host='0.0.0.0', port=4444)
