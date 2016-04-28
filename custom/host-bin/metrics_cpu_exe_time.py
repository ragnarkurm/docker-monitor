import os

def metrics(prev):
	base = '/proc'
	items = os.listdir(base)
	stats = {}
	for f in items:
		try:
			if not f.isdigit():
				continue
			pid = base + '/' + f
			if not os.path.isdir(pid):
				continue
			exe = pid + '/exe'
			if not os.path.islink(exe):
				continue
			exe = os.path.realpath(exe)
			exe = exe.rsplit('/', 1)
			exe = exe[1]
			stat = pid + '/stat'
			f = open(stat, 'r')
			stat = f.readline()
			f.close()
			stat = stat.split(' ')
			time = int(stat[13]) + int(stat[14]) # utime + stime
			if exe not in stats:
				stats[exe] = 0
			stats[exe] = stats[exe] + time
		except Exception as e:
			#print e
			continue

	data = {}
	for exe in stats:
		if not exe in prev:
			continue
		diff = stats[exe] - prev[exe]
		if diff <= 0: # sometimes negative if some process exits
			continue
		data[exe] = {
			'measurement': 'cpu_exe_time',
			'tags': {
				'exe': exe,
			},
			'fields': {
				'value': diff,
			},
		}

	data = data.values()

	return [stats, data]
