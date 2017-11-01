import json
import yaml

def load_config(value):
    with open('config.yml') as f:
        data = yaml.load(f)
    return data[value]

def create_input_vrpd(users, distance_matrix):
    data = {}
    data['instance_name'] = 'test'
    data['max_vehicle_number'] = 25
    data['vehicle_capacity'] = 200.0

    # Creating deport part
    coordinates = {}
    deport = {}
    coordinates['x'] = users[0]['pickup']['coordinates'][0]
    coordinates['y'] = users[0]['pickup']['coordinates'][1]
    deport['coordinates'] = coordinates
    deport['demand'] = 0.0
    deport['due_time'] = 1235.0
    deport['ready_time'] = 0.0
    deport['service_time'] = 0.0
    data['deport'] = deport
    
    # Creating Customer deleivery part
    count = 1
    for user in users:
        coordinates = {}
        deport = {}
    	coordinates['x'] = user['delivery']['coordinates'][0]
    	coordinates['y'] = user['delivery']['coordinates'][1]
    	deport['coordinates'] = coordinates
    	deport['demand'] = 0.0
    	deport['due_time'] = 1236.0
    	deport['ready_time'] = 0.0
    	deport['service_time'] = 0.0
        deport['_id'] = user['_id']
    	data['customer_'+str(count)] = deport
        count += 1
    
    # appending distance matrix
    data['distance_matrix'] = distance_matrix
    
    with open('/usr/src/app/py-ga-VRPTW/data/json/input.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
    return count
