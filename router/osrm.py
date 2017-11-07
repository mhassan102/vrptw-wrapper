import requests
import yaml
import json

def load_config(value):
    with open('config.yml') as f:
        data = yaml.load(f)
    return data[value]

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


def get_route_distance(lat1, long1, lat2, long2):
    headers = {'User-Agent': 'User-Agent verification if any'}
    url = load_config('osrm_route_url') + \
		str(lat1) + ',' + str(long1) + ';' + str(lat2) + ',' + str(long2)
    print url
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data['routes'][0]['distance']
