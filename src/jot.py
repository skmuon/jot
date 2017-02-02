#!/bin/python

"""
Goal - Develop a simple tool to log all work related activities

"""

import sys
import datetime

# Work log file
wlf = "worklog.txt"
separator = "\n----------------------------------------------------------------------\n\n"

# Prepends new lines to top of the file
def prepend_line(file, line):
	with open(file, 'r+') as f:
		content = f.read()
		f.seek(0,0)
		f.write(line.rstrip('\r\n') + '\n' + content)


"""
Log format:
        The user provided information will be logged in the following format
	[Date],[Time],[String]
"""

# Prompt user to input data, Uses Q/q to quit
while 1:
	now = datetime.datetime.now()
	flog = now.strftime("%Y-%m-%d  %H:%M") + ","
	log = raw_input(">> ")
	if log in ["Q", "q"]: break;
	flog += log + ","
	prepend_line(wlf, flog + '\n');

# Add separator
prepend_line(wlf, separator)
