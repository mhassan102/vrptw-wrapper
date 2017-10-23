import requests
import json
from definations import *

def osrm_client(users):
	headers = {'User-Agent': 'User-Agent verification if any'}
	url = load_config('osrm_url') + \
		str(users[0]['pickup']['coordinates'][0]) + ',' + str(users[0]['pickup']['coordinates'][1]) + ';'
	for user in users:
		url = url + \
		str(user['delivery']['coordinates'][0]) + ',' + str(user['delivery']['coordinates'][1]) + ';'
	url = url.rstrip(';')
	response = requests.get(url)
	json_data = json.loads(response.text)
	return json_data['durations']
