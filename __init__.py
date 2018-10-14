# __init__.py

from flask import Flask

# blueprints
from routes import routes

from flask_pymongo import PyMongo


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
mongo = PyMongo(app)

app.register_blueprint(routes)


