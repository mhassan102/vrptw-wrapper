import json
import requests

headers = {'Content-Type': 'application/json'}
print headers
payload = { "users" : [
{ "_id": {
	"$oid": "59e9f0888773be6769878fff"
	},
"status": "prospect",
"valid_until": {
	"$date": "2017-10-23T12:00:00.000Z"
	},
"project_id": 3009,
"deliveryprice_id": "572482a3b29b59c46597eac5",
"advanced_pickup": True,
"quote_id": "59e9f0408773be6769878e28",
"pickup_reference": "TM966",
"window": 120,
"type": "interval",
"price_ex_mva": 79.2,
"price": 99,
"module": "argus",
"weight": 3.24,
"user_id": "560a39144486a50752cedf10",
"delivery": {
	"address": {
		"city": "OSLO",
		"country": "Norge",
		"street": "Dalenenggata 14A",
		"zip": 567
		},
	"customer": {
		"firstname": "Marte",
		"lastname": "Olaisen",
		"companyname": "",
		"midname": ""
		},
	"contact": {
		"email": " martehol@gmail.com",
		"phone": "95943224"
		},
	"coordinates": [
		10.6996406577,
		59.9395214378
		]
	},
"pickup": {
	"address": {
		"city": "Oslo",
		"country": "Norge",
		"street": "Karenslyst Alle 9",
		"zip": 278
		},
	"customer": {
		"companyname": "MENY Skoyen",
		"firstname": "",
		"midname": "",
		"lastname": "Utleveringsansvarlig"
		},
	"contact": {
		"email": "",
		"phone": "23276900"
		},
	"coordinates": [
		10.6836406577,
		59.9205214378
		]
	},
"restrictions": 'Null',
"dates": {
	"pickup": {
		"$date": "2017-10-23T12:00:00.000Z"
		},
	"delivery": {
		"$date": "2017-10-23T14:00:00.000Z"
		}
	},
"basket": [],
"special_goods": [
	2
	],
"invoice": {
	"generated": False
	},
"__v": 0,
"foreign_id": "78322" }
,
{"_id": {
	"$oid": "59e9f0888773be6769878ebf"
	},
"status": "prospect",
"valid_until": {
	"$date": "2017-10-23T12:00:00.000Z"
	},
"project_id": 3009,
"deliveryprice_id": "572482a3b29b59c46597eac5",
"advanced_pickup": True,
"quote_id": "59e9f0408773be6769878e28",
"pickup_reference": "TM966",
"window": 120,
"type": "interval",
"price_ex_mva": 79.2,
"price": 99,
"module": "argus",
"weight": 3.24,
"user_id": "560a39144486a50752cedf10",
"delivery": {
	"address": {
		"city": "OSLO",
		"country": "Norge",
		"street": "Dalenenggata 14A",
		"zip": 567
		},
	"customer": {
		"firstname": "Marte",
		"lastname": "Olaisen",
		"companyname": "",
		"midname": ""
		},
	"contact": {
		"email": " martehol@gmail.com",
		"phone": "95943224"
		},
	"coordinates": [
		10.6936406577,
		59.9305214378
		]
	},
"pickup": {
	"address": {
		"city": "Oslo",
		"country": "Norge",
		"street": "Karenslyst Alle 9",
		"zip": 278
		},
	"customer": {
		"companyname": "MENY Skoyen",
		"firstname": "",
		"midname": "",
		"lastname": "Utleveringsansvarlig"
		},
	"contact": {
		"email": "",
		"phone": "23276900"
		},
	"coordinates": [
		10.6836406577,
		59.9205214378
		]
	},
"restrictions": 'Null',
"dates": {
	"pickup": {
		"$date": "2017-10-23T12:00:00.000Z"
		},
	"delivery": {
		"$date": "2017-10-23T14:00:00.000Z"
		}
	},
"basket": [],
"special_goods": [
	2
	],
"invoice": {
	"generated": False
	},
"__v": 0,
"foreign_id": "78322"}
]
}
r = requests.post("http://127.0.0.1:5000/route", data=json.dumps(payload), headers=headers)
print r

