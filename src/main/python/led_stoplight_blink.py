import RPi.GPIO as GPIO
import time

RED=15
YELLOW=11
GREEN=7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)

def Blink(numTimes, speed):
	for i in range(0,numTimes):
		print "Iteration " + str(i+1)
		GPIO.output(GREEN, True)
		time.sleep(speed)
		GPIO.output(GREEN, False)
		time.sleep(speed)
		GPIO.output(YELLOW, True)
		time.sleep(speed)
		GPIO.output(YELLOW, False)
		time.sleep(speed)
		GPIO.output(RED, True)
		time.sleep(speed)
		GPIO.output(RED, False)
		time.sleep(speed)
	print "Done"
	GPIO.cleanup()

iterations = raw_input("Enter total number of times to blink: ")
speed = raw_input("Enter seconds for each blink: ")

Blink(int(iterations),float(speed))
