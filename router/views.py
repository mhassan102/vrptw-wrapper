import os
import socket
from flask import Blueprint, request
from osrm import osrm_client
from definations import *
from vrptw import vrptw_route 

api = Blueprint('api', __name__)

@api.route("/route", methods = ['POST'])
def route():
	distance_matrix = osrm_client(request.json['users'])
	input_json = create_input_vrpd(request.json['users'], distance_matrix)
	vrptw_route(input_json)
    	return "Router app"


