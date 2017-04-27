import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

GPIO.output(7,True)
GPIO.output(11,False)
GPIO.output(15,True)
GPIO.output(13,False)
sleep(1)
GPIO.cleanup()
