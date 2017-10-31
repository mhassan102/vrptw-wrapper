import json

INPUT_PATH='/usr/src/app/py-ga-VRPTW/data/json/input.json'

def route_map(route):
    with open(INPUT_PATH) as data_file:    
        data = json.load(data_file)
        for row in range(len(route)):
            for col in range(len(route[row])):
                prev_id = route[row][col]
                route[row][col] = data['customer_%d' % prev_id]['_id']
    return route


def order_map(order):
    with open(INPUT_PATH) as data_file:    
        data = json.load(data_file)
        for index in range(len(order)):
            prev_id = order[index]
            order[index] = data['customer_%d' % prev_id]['_id']
    return order
