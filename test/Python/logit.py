#!/usr/bin/env python
#level 3 - info
#level 2 - debug
#level 1 - trace
import sys

logLevel = int(sys.argv[1])

def logit(level, msg):
	if level >= logLevel:
		print 'MSG' + str(level) + ':', msg
		
def getUser():
	logit(2, 'Entering Function getUser()...')
	user = raw_input('Enter User Name: ')
	logit(1, 'Leaving Function getUser()...')
	return user
	
logit(3, 'Starting Script...')
logit(3, 'User Entered: ' + getUser())
logit(3, 'Ending Script.')