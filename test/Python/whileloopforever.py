#!/usr/bin/env python
#loop until user terminates wtih Ctrl + C
import time

counter = 0;

while 1:
	time.sleep(1)
	counter += 1
	
	print 'Script has been looping for', counter, 'seconds...'