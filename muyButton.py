import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
GPIO.setup(4, GPIO.OUT)



while true:
	btnInput = GPIO.input(24)
	if btnInput == True:
		print("Pressed")
	else:
		print("Released")
	time.sleep(1)