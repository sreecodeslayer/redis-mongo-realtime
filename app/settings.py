from flask_mongoengine import MongoEngine
from walrus import Walrus

DB_ENGINE = MongoEngine()
WALRUS_DB = Walrus(host='127.0.0.1', port=6379, db=5)