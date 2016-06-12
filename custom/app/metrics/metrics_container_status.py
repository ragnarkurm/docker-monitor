import subprocess

def metrics():

	lines = subprocess.check_output(["/usr/bin/docker", "ps", "-a", "--format", "{{.Status}}"], universal_newlines=True)
	lines = lines.splitlines()
	status = {}
	for l in lines:
		l = l.partition(" ")[0]
		if l in status:
			prev = status[l]
		else:
			prev = 0
		status[l] = prev + 1

	for s in status:
		status[s] = {
			'measurement': 'container_status',
			'tags': {
				'status': s,
			},
			'fields': {
				'value': status[s],
			},
		}

	data = status.values()

	return data
