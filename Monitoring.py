class Monitoring:

	lines = []
	tags = {}
	db = {
		'host': '',
		'port': 0,
		'name': '',
		'user': '',
		'pass': '',
		'precision': '',
		'rp': '',
	}
	auth = None

	def __init__(self, conffile):
		import ConfigParser
		cp = ConfigParser.ConfigParser()
		result = cp.read(conffile)
		if len(result) <> 1:
			raise Exception('Unable to read configuration file: ' + conffile)
		
		section = 'Database'
		for k, v in self.db.iteritems():
			if type(v) == str:
				self.db[k] = cp.get(section, k)
			elif type(v) == int:
				self.db[k] = cp.getint(section, k)
			elif type(v) == float:
				self.db[k] = cp.getfloat(section, k)
			else:
				raise Exception('Unexpected type in conf: ' + str(type(v)))

		section = 'Tags'
		tags = cp.items(section)
		for t in tags:
			self.tags[t[0]] = t[1]

		params = {
			'db': self.db['name'],
			'u': self.db['user'],
			'p': self.db['pass'],
			'precision': self.db['precision'],
			'rp': self.db['rp'],
		}
		params = ['{}={}'.format(k, v) for k, v in params.iteritems()]
		params = '&'.join(params)
		self.url='http://{}:{}/write?{}'.format(self.db['host'], self.db['port'], params)

		from requests.auth import HTTPBasicAuth
		self.auth=HTTPBasicAuth(self.db['user'], self.db['pass'])


	def collect_many(self, data):

		for d in data:

			measurement = d['measurement']

			fields = d['fields']

			if 'tags' in d:
				tags = d['tags']
			else:
				tags = {}

			if 'timestamp' in d:
				timestamp = d['timestamp']
			else:
				timestamp = None

			self.collect(measurement, tags, fields, timestamp)

	def collect(self, measurement, tags, fields, timestamp = None):

		if False: # debug
			print measurement
			print tags
			print fields
			print timestamp
			return

		line = ""

		line = line + measurement

		tags2 = self.tags.copy()
		tags2.update(tags)
		tags2 = ['{}={}'.format(k, v) for k, v in tags2.iteritems()]
		tags2 = ','.join(tags2)
		line = line + ',' + tags2

		fields2 = []
		for k, v in fields.iteritems():
			if type(v) is int:
				v = str(v) + 'i'
			elif type(v) is float:
				v = str(v)
			else:
				raise Exception('Unexpected type in conf: ' + str(type(v)))
			kv = '{}={}'.format(k, v)
			fields2.append(kv)
		fields2 = ','.join(fields2)
		line = line + ' ' + fields2

		if type(timestamp) is int:
			line = line + ' ' + str(timestamp)

		self.lines.append(line)

	def send(self):

		import requests

		data = "\n".join(self.lines)

		r = requests.post(
			url=self.url,
			auth=self.auth,
			data=data,
		)

		if r.status_code != 204:
			raise Exception("Transaction failed.\n" + r.url + "\n" + r.text)

		self.lines = []

# from Monitoring import Monitoring
# m = Monitoring('monitor.conf')
# m.collect(
# 	'testing_measurement',
# 	{
# 		'disk': 'sda',
# 	},
# 	{
# 		'usage': 92.58,
# 	},
# 	1465405362
# )
# m.send()
