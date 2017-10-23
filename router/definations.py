import json
import yaml

def load_config(value):
    with open('config.yml') as f:
        data = yaml.load(f)
    return data[value]

def create_input_vrpd(users, distance_matrix):
    data = {}
    data['instance_name'] = 'hassan'
    data['max_vehicle_number'] = 25
    data['vehicle_capacity'] = 200.0

    # Creating deport part
    coordinates = {}
    coordinates['x'] = 13.0
    coordinates['y'] = 52.0
    deport = {}
    deport['coordinates'] = coordinates
    deport['demand'] = 0.0
    deport['due_time'] = 1236.0
    deport['ready_time'] = 0.0
    deport['service_time'] = 0.0
    data['deport'] = deport

    # Creating Customer deleivery part
    count = 1
    for user in users:
    	coordinates['x'] = user['delivery']['coordinates'][0]
    	coordinates['y'] = user['delivery']['coordinates'][1]
    	deport['coordinates'] = coordinates
    	deport['demand'] = 0.0
    	deport['due_time'] = 1236.0
    	deport['ready_time'] = 0.0
    	deport['service_time'] = 0.0
    	data['customer_'+str(count)] = deport
        count += 1

    # appending distance matrix
    data['distance_matrix'] = distance_matrix
    json_data = json.dumps(data)
    with open('/usr/src/app/py-ga-VRPTW/data/json/input.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)

