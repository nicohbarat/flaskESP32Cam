#!/usr/bin/python
# coding: utf-8
import os
from datetime import datetime
from flask import Flask,jsonify,request
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def entry_point():
	return jsonify(message = 'Selamat datang di Root!')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    image = request.files['image']
    filename = f"{UPLOAD_FOLDER}/photo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    image.save(filename)

    # Dummy deteksi
    detected_object = "bottle"

    return jsonify({"object": detected_object})
	



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000,debug=True)
	
