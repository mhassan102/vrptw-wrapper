import os
import socket
from flask import Blueprint, request, jsonify
from osrm import osrm_client
from definations import *
from vrptw import vrptw_route 

api = Blueprint('api', __name__)

@api.route("/route", methods = ['POST'])
def route():
    try:
	distance_matrix = osrm_client(request.json['users'])
	input_json = create_input_vrpd(request.json['users'], distance_matrix)
	return jsonify(vrptw_route(input_json))
    except Exception as e:
        return "Api is failing with error: " + str(e)

