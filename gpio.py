import CHIP_IO.GPIO as GPIO
import time
GPIO.setup("XIO-P0", GPIO.IN)

while True:
	x = GPIO.input("XIO-P0")
	if x==0:
        	print "%s there is some thing act:%d" % (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),x)
		time.sleep(0.5)
	time.sleep(0.01)
