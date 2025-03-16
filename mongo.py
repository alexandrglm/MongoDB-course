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
@app.route('/films', methods=['POST'])
def post_film():

    data = request.json

    if not data:
        return jsonify( {"error", "Cannot POST, no data provided"} ), 400
    
    # .insert_one() Method
    result = film_collection.insert_one(data)


## GET ALL endpoint
@app.route('/films', methods=['GET'])
def get_all():

    # find() Method
    films = list(film_collection.find())

    if not films:
        return jsonify( {"error", "Cannot GET ALL, no data retuned"} ), 400

    for film in films:

        # item[the id but _protected]
        film['_id'] = str(film['_id'])

    return jsonify(films)



## GET endpoint
@app.route('/films/<film_id>', methods=['GET'])
def get_one(film_id):

    film = film_collection.find_one( { "_id" : ObjectId(film_id) } )

    if not film:
        return jsonify( {"error", "Cannot GET ONE, no data retuned"} ), 400

    film['_id'] = str(film['_id'])
    return jsonify(film)



## DELETE ONE endpoint
@app.route('/films/<film_id>')
def delete_one(film_id):

    # delete_one()
    result = film_collection.delete_one( { "_id" : ObjectId(film_id) } )

    if result.deleted_count is not 0:
        
        return jsonify( { "status" : "Success" } )

    else:

        return jsonify( { "error" : "Object not found" }, 400 )
    

#################################
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
