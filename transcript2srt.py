#!/usr/local/bin/python
import sys
from datetime import datetime,timedelta

lines = [ l for l in open(sys.argv[1]) ]

def get_beginning(line):
	return datetime.strptime( line[0:8] , "%H:%M:%S" )

for i,line in enumerate(lines):
	init = get_beginning(line)
	
	if i+1 < len(lines):
		next_init = get_beginning(lines[i+1]) - timedelta(milliseconds=125)
	else:
		next_init = init + timedelta(seconds=10)
	
	print i+1
	print "%s,000 --> %s,950" % (init.strftime("%H:%M:%S"), next_init.strftime("%H:%M:%S"))
	print line[11:]
	
