# routes.py

from flask import Blueprint

from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from bson.json_util import dumps 

routes = Blueprint('routes', __name__)



############
## Trumpets
############


## Retrieve all trumpets 
@app.route('/trumpets', methods=['GET'])
def get_all_trumpets():
    trumpets = mongo.db.trumpet.find()
    return dumps(trumpets)


## Retrieve all non-reply trumpets
@app.route('/trumpets_main', methods=['GET'])
def get_all_main_trumpets():
    trumpets = mongo.db.trumpet.find( { "reply_trumpet_id": null } )
    return dumps(trumpets)


## Retrieve trumpet with given ObjectID
@app.route('/trumpets/:trumpet_id', methods=['GET'])
def get_trumpet(trumpet_id):
    trumpet = mongo.db.trumpet.find_one( { "_id": trumpet_id } )
    return dumps(trumpet)


## Increment the like count of a trumpet with given ObjectID by 1
@app.route('/trumpets/:trumpet_id/likes', methods=['GET'])
def increment_likes(trumpet_id):
    mongo.db.trumpet.update(
        { "_id": trumpet_id },
        { $inc: { "likes": +1 } }
    )


## Increment the retrumpet count of a trumpet with given ObjectID by 1
@app.route('/trumpets/:trumpet_id/retrumpets', methods=['GET'])
def increment_retrumpets(trumpet_id):
    mongo.db.trumpet.update(
        { "_id": trumpet_id },
        { $inc: { "retrumpets": +1 } }
    )


## Increment the reply count of a trumpet with given ObjectID by 1
@app.route('/trumpets/:trumpet_id/replies', methods=['GET'])
def increment_replies(trumpet_id):
    mongo.db.trumpet.update(
        { "_id": trumpet_id },
        { $inc: { "replies": +1 } }
     )


## Create a new non-reply trumpet
@app.route('/trumpets', methods=['POST'])
def post_trumpet(user_info_id, submit_time, text):
    mongo.db.trumpet.insert_one(
        { "user_info_id":, user_info_id,
          "reply_trumpet_id": null,
          "submit_time": submit_time,
          "text": text,
          "likes": 0,
          "retrumpets": 0,
          "replies": 0 }
    )


## Create a new reply trumpet
@app.route('/trumpets', methods=['POST'])
def post_trumpet(user_info_id, submit_time, text, reply_trumpet_id):
    mongo.db.trumpet.insert_one(
        { "user_info_id":, user_info_id,
          "reply_trumpet_id": reply_trumpet_id,
          "submit_time": submit_time,
          "text": text,
          "likes": 0,
          "retrumpets": 0,
          "replies": 0 }
    )


## Delete an existing trumpet
@app.route('/trumpets/:trumpet_id', methods=['DELETE'])
def delete_trumpet(trumpet_id):
    mongo.db.trumpet.delete_one( { "_id": trumpet_id } ) 
