# Utility functions
ENV_FILENAME = '.env'

def readenvline(line, dictionary):
	# @param line: string of form 'key=value', no spaces
	# Parse and insert line into 'dicionary'
	try:
		envvar = line.replace(' ', '').strip().split('=')
		dictionary[envvar[0]] = envvar[1]
	except IndexError:
		# incorrect format
		print "Incorrect format for environment variable in line '{}'".format(line)

def readenv():
	# read env variables into dictionary and return
	d = {}
	with open(ENV_FILENAME, 'r') as f:
		for line in f:
			readenvline(line, d)
	return d
