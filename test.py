import requests
import time

import logging
import sys

logger = logging.getLogger('Realtime-tester')

ch = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
	'%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)

mongo_req = 'http://localhost:8000/mongo_add_user'
redis_req = 'http://localhost:8000/redis_add_user'
data = {
	'username':'Sreenadh',
	'password':'Sreenadh',
	'age':23,
	'dob':'1994-11-25',
	'place':'kannur'
}
# logger.debug("Sending add user to MongoDB using data: {}".format(data))
# resp_time = 0
# for _ in range(10000):
# 	st_time = time.time()
# 	logger.debug("Start time: {}".format(
# 		time.strftime('%H:%M:%S', time.localtime(st_time))
# 		)
# 	)
# 	resp = requests.post(mongo_req, json=data)
# 	en_time = time.time()
# 	logger.debug("End time: {}".format(
# 		time.strftime('%H:%M:%S', time.localtime(en_time))
# 		)
# 	)
# 	resp_time += (en_time - st_time)


# logger.debug("Total Time: {}".format(resp_time))
logger.debug("Sending add user to Redis using data: {}".format(data))
resp_time = 0
for _ in range(1000000):
	st_time = time.time()
	logger.debug("Start time: {}".format(
		time.strftime('%H:%M:%S', time.localtime(st_time))
		)
	)
	resp = requests.post(redis_req, json=data)
	en_time = time.time()
	logger.debug("End time: {}".format(
		time.strftime('%H:%M:%S', time.localtime(en_time))
		)
	)
	resp_time += (en_time - st_time)


logger.debug("Total Time: {}".format(resp_time))