#!/usr/bin/python2.7-cgi

import os
import threading, time, datetime
import RPi.GPIO as GPIO
import time
#GPIO.cleanup()
pinLED = [14,15,18,23,24,25,8,7,12,16]
GPIO.setmode(GPIO.BCM)

for i in range(len(pinLED)):
	GPIO.setup(pinLED[i],GPIO.OUT)

def main():
	content = ''
	try:
		oldTime = time.time()
		while 1:
			t = time.strftime("%Y%m%d_%H%M%S", time.localtime())
			os.system("git pull")
			if os.path.isfile('2.txt'): 
				with open('2.txt', 'r') as file :
					content = file.readline()
					print('[' + t + ']--[' + content + ']')
			content = content.split(',')
			for i in range(1, len(content)):
				if i == int(content[i]):
					GPIO.output(pinLED[i-1],1)
				else:
					GPIO.output(pinLED[i-1],0)
			time.sleep(1)
			if (time.time() - oldTime) >= 500:break
	except KeyboardInterrupt:
		pass
		GPIO.cleanup()			
	GPIO.cleanup()	
	
main()	
#t = threading.Thread(target = job)
#t.setDaemon(True)
#t.start()	

					
