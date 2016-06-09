keys = [
	"id",
	"user",
	"nice",
	"system",
	"idle",
	"iowait",
	"irq",
	"softirq",
	"steal",
	"guest",
	"guest_nice",
]

import re
def metrics():

	f = open('/proc/stat', 'r')
	line = f.readline()
	f.close()

	line = line.strip()
	values = re.split('\s+', line)
	data = dict(zip(keys, values)) 
	del data["id"]

	for k in data:
		data[k] = {
			'measurement': 'cpu_task_time',
			'tags': {
				'task': k,
			},
			'fields': {
				'value': int(data[k]),
			},
		}

	return data.values()
