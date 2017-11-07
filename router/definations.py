import json
from osrm import get_route_distance


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

    
def manual_calculated(input_json):
    distance_matrix = []
    coordinates_array = []
    pickup_x = input_json[0]['pickup']['coordinates'][0]
    pickup_y = input_json[0]['pickup']['coordinates'][1]
    coordinates_array.append([pickup_x, pickup_y])  
 
    for user in input_json:
        delivery_x = user['delivery']['coordinates'][0]
    	delivery_y = user['delivery']['coordinates'][1]
        coordinates_array.append([delivery_x, delivery_x])  
      
    for outer_points in coordinates_array:
        row = []
        for inner_points in coordinates_array: 
            distance = get_route_distance(outer_points[0], outer_points[1], inner_points[0], inner_points[1])
            row.append(distance)
            print row
         
        distance_matrix.append(row)
    return distance_matrix 
