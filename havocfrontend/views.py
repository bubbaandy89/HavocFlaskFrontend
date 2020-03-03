#!/usr/bin/env python
from havocfrontend import app

@app.route('/')
def index():
    return 'Hello World!'
