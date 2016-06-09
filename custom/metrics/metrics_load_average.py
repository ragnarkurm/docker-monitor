import os

def metrics():
	f = open('/proc/loadavg', 'r')
	line = f.readline()
	f.close()
	load = line.split(' ')
	load1 = float(load[0])
	load5 = float(load[1])
	load15 = float(load[2])
	data = [
		{
			'measurement': 'load_average',
			'tags': {
			},
			'fields': {
				'value': load1,
				'value5': load5,
				'value15': load15,
			},
		}
	]
	return data
