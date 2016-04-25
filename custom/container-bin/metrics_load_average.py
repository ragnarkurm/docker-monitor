import os

def metrics():
	load = os.getloadavg()[0]
	data =[
		{
			'measurement': 'load_average',
			'tags': {
			},
			'fields': {
				'value': load
			}
		}
	]
	return data
