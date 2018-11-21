import RPi.GPIO as GPIO
import time
import request

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
GPIO.setup(4, GPIO.OUT)

print "OK"