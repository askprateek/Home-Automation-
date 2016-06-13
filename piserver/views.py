from django.http import HttpResponse

import RPi.GPIO as GPIO
import time
import serial

LED1 = 22
LED2 = 19
FAN1 = 18
FAN2 = 21
BUZZER=17
WATER_SPRINKLER= 23
state= True
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

def turnon(request):
	GPIO.setup(22, GPIO.OUT)
	GPIO.output(22,True)
	html= "Light is on"
	return HttpResponse(html)
			

def turnoff(request):
	GPIO.setup(22, GPIO.OUT)
	GPIO.output(22,False)
	html= "Light is off"
	return HttpResponse(html)

		
def led2(request):
	GPIO.output(17,True)
	html= "Light 2 on"
	return HttpResponse(html)

def led2off(request):
	GPIO.output(17,False)
	html= "Light 2 off"
	return HttpResponse(html)

