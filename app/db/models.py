from app.settings import DB_ENGINE, WALRUS_DB
import walrus

class UserMongo(DB_ENGINE.Document):
	username = DB_ENGINE.StringField()
	password = DB_ENGINE.StringField()
	age = DB_ENGINE.IntField()
	place = DB_ENGINE.StringField()
	dob = DB_ENGINE.DateTimeField()

class UserRedis(walrus.Model):
	__database__ = WALRUS_DB
	_id = walrus.AutoIncrementField(walrus.IntegerField)
	username = walrus.TextField()
	password = walrus.TextField()
	age = walrus.IntegerField()
	place = walrus.TextField()
	dob = walrus.DateTimeField()