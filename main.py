#!/usr/bin/python
# coding: utf-8
from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route('/')
def entry_point():
	return jsonify(message = 'Selamat datang di Root!')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000,debug=True)
	
