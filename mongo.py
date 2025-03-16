############################################################################
# MongoDB-course
#
############################################################################
# Back-end for MongoDB-Course
#
# Subject: A film library db with my favourites films and their data
#
# Requirements:
# - Flask
#
# Pending to decide which Mongo modules will be used:
# - PyMongo
# - MongoEngine
#################################
from flask import Flask, render_template, send_from_directory, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId
#################################
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def statics(filename):

    return send_from_directory('static', filename)
#################################
# MongoDB back-end setups
client = MongoClient('mongodb://localhost:27017')
db = client['db']

# Collections
film_collection = db['filmLibrary']
#################################
# Endpoints routes
## POST endpoint
# @app.route('/filmLibrary')

## GET ALL endpoint
# @app.route('/filmLibrary')

## GET endpoint
# @app.route('/filmLibrary/<film_id>', methods=['GET'])
# def get_endpoint():
#    book = books_collection

## DELETE endpoint
#@app.route('/filmLibrary/<film_id>')



#################################
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
