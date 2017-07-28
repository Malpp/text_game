#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import os
from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/")
def hello():
	return "Hello World!"

if __name__ == '__main__':
	port = int(os.getenv('PORT', 5000))
	app.run(debug=True, port=port, host='0.0.0.0')
