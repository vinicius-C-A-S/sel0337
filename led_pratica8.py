import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)

while True :
	GPIO.output(15, True)
	sleep(0.2)
	GPIO.output(15, False)
	sleep(0.2)