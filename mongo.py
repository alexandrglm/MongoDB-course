############################################################################
# MongoDB-course
#
############################################################################
# Back-end for MongoDB-Course
#
# Requirements:
# - Flask
#
# Pending to decide which Mongo modules will be used:
# - PyMongo
# - MongoEngine
#################################
from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId
#################################
app = Flask(__name__)
#################################




#################################
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
