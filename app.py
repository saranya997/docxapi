import nltk

try:
	nltk.data.find('tokenizers/punkt')
except LookupError:
	nltk.download('punkt')
	nltk.download('stopwords')

import process
import os
from flask_cors import CORS, cross_origin
from flask import Flask, flash, request, redirect, url_for, send_from_directory, Response, jsonify, json, send_file,session


app = Flask(__name__)
app.secret_key = "super secret key"
CORS(app)


		   
@app.route('/search', methods=['GET', 'POST'])
def search():
	print(request.method)
	print(request.args.get('term'))
	status = process.searchdoc(request.args.get('term'))
	return jsonify(
        status= "success",
        message= "search successful",
        code= 200,
        data= status
    )
		   
		   
@app.route('/', methods=['GET', 'POST'])
def index():
	return "unauthorised access"
	