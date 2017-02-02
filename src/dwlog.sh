#!/bin/bash

# Displays working log

# Get the date filter
wfile="worklog.txt"
dfilter=$1

if [ -f $wfile ]; then
	cat $wfile | grep "$dfilter" | awk -F "," '{print $2}'
fi
