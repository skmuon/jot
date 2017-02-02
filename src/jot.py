#!/bin/python


"""
Goal - Develop a simple tool to log all work related activities

"""

import sys
import datetime

wlf = "worklog.txt"
separator = "\n\n----------------------------------------------------------------------\n\n"

def prepend_line(file, line):
	with open(file, 'r+') as f:
		content = f.read()
		f.seek(0,0)
		f.write(line.rstrip('\r\n') + '\n' + content)


"""
Log format:
	[Date],[Time],[String]
"""

while 1:
	now = datetime.datetime.now()
	flog = now.strftime("%Y-%m-%d  %H:%M") + ","
	log = raw_input(">> ")
	if log in ["Q", "q"]: break;
	flog += log + ","
	prepend_line(wlf, flog + '\n');

prepend_line(wlf, separator)
