from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Device
from django.core import serializers
import RPi.GPIO as GPIO
import time
import serial ,requests

#BUZZER=17
BUZZER_CHECK1=5
BUZZER_CHECK2=9
BUZZER_PIN1=6			#BUZZER OPERATION
BUZZER_PIN2=13
#WATER_SPRINKLER= 23
state= True
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

def device(request,type,id,status):
    device = Device.objects.get(type=type, device_id = id)
    GPIO.setup(device.pin_no, GPIO.OUT)
    status=int(status)
    if status:
	GPIO.output(device.pin_no, True)
    else:
	GPIO.output(device.pin_no, False)
		
    device.status = status
    device.save()
    html = device
    #return HttpResponse(html)
    
    return HttpResponse( type + str(id) + str(status) )

def buzzer(request):
	pass

def temp(request):
	ser= serial.Serial('/dev/ttyACM0',57600)
	
	while 1:
		a = ser.readline()
		x = a.split(':')
		if x[0]=="Temperature":
			break

	return HttpResponse(x[1])

def status(request):
	device_status = serializers.serialize('json', Device.objects.all())
	return HttpResponse(device_status)

def allon(request):
	GPIO.setup(FAN1, GPIO.OUT)
	GPIO.output(FAN1,False)
	GPIO.setup(FAN2,GPIO.OUT)
	GPIO.output(FAN2, False)
	GPIO.setup(LED1, GPIO.OUT)
	GPIO.output(LED1,False) 
	GPIO.setup(LED2,GPIO.OUT)
	GPIO.output(LED2, False)
	return HttpResponse("ALL ON ")

def alloff(request):
	GPIO.setup(FAN1, GPIO.OUT)
	GPIO.output(FAN1, True)
	GPIO.setup(FAN2,GPIO.OUT)
	GPIO.output(FAN2, True)
	GPIO.setup(LED1, GPIO.OUT)
	GPIO.output(LED1, True) 
	GPIO.setup(LED2,GPIO.OUT)
	GPIO.output(LED2, True)	
	return HttpResponse("ALL OFF ")

def lockdown(request):
	alloff(request)
	url = 'http://192.168.0.2:3000/' # Buzzer Url
	send = requests.get(url, verify = False)
	
	return HttpResponse("Lockdown")