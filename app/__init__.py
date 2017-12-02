from flask import Flask, request, jsonify
from app.settings import DB_ENGINE

from app.db.models import UserMongo,UserRedis
from datetime import datetime
import time

application = Flask(__name__, instance_relative_config = True)
application.config.from_envvar('REALTIME_APP_SETTINGS')

DB_ENGINE.init_app(application)


@application.route('/mongo_add_user', methods = ['POST'])
def mongo_add_user():
	try:
		data = request.get_json()

		username = data.get('username')
		password = data.get('password')
		age = data.get('age')
		place = data.get('place')
		dob = data.get('dob')

		assert username
		assert password
		assert age
		assert place
		assert dob
	except AssertionError as e:
		return jsonify(
			status=False,
			reason="Invalid request"
		), 400

	try:
		st_time = time.time()
		user = UserMongo()
		user.username = username
		user.password = password
		user.age = age
		user.place = place
		user.dob = dob
		user.save()
		en_time = time.time()

		return jsonify(
			status = True,
			uid = str(user.id),
			time = en_time - st_time
		)
	except Exception as e:
		raise e

@application.route('/redis_add_user', methods = ['POST'])
def redis_add_user():
	try:
		data = request.get_json()

		username = data.get('username')
		password = data.get('password')
		age = data.get('age')
		place = data.get('place')
		dob = data.get('dob')

		assert username
		assert password
		assert age
		assert place
		assert dob
	except AssertionError as e:
		return jsonify(
			status=False,
			reason="Invalid request"
		), 400

	try:
		st_time = time.time()
		user = UserRedis.create(
		username = username,
		password = password,
		age = age,
		place = place,
		dob = datetime.strptime(dob,'%Y-%m-%d')
		)
		en_time = time.time()

		return jsonify(
			status = True,
			uid = str(user._id),
			time = en_time - st_time
		)
	except Exception as e:
		raise e