from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Fan,Led
import RPi.GPIO as GPIO
import time
import serial ,requests

LED1 = 22
LED2 = 19
FAN1 = 18
FAN2 = 21
#BUZZER=17
BUZZER_CHECK1=5
BUZZER_CHECK2=9
BUZZER_PIN1=6			#BUZZER OPERATION
BUZZER_PIN2=13
#WATER_SPRINKLER= 23
state= True
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

def led(request,led_id,status):
	lid = int(led_id)
	status = int(status)
	if lid ==1 and status ==0 :
		GPIO.setup(LED1, GPIO.OUT)
		GPIO.output(LED1,True) 			#LIGHT ONE ON
		a = "11"
	elif lid ==1 and status ==1 :
		GPIO.setup(LED1, GPIO.OUT)
		GPIO.output(LED1,False)			#LIGHT 1 OFF
		a = "10"

	elif lid ==2 and status ==0 :	
		GPIO.setup(LED2, GPIO.OUT)
		GPIO.output(LED2, True)			#LIGHT 2 ON	
		a = "21"
	elif lid ==2 and status ==1 :
		GPIO.setup(LED2,GPIO.OUT)
		GPIO.output(LED2, False)		#LIGHT 2 OFF\
		a = "20"
	a = Led.objects.get(led_id = lid)
	a.status = status
	a.save()
	return HttpResponse(a.status)

	#html=  "led " + led_id + " " + status
	#return HttpResponse(html)

def fan(request, fan_id, status):
	fan_id = int(fan_id)
	status=int(status)
	if fan_id ==1 and status ==0 :
		GPIO.setup(FAN1, GPIO.OUT)
		GPIO.output(FAN1,True) 			#FAN ONE ON

	elif fan_id ==1 and status ==1 :
		GPIO.setup(FAN1, GPIO.OUT)
		GPIO.output(FAN1,False)			#FAN 1 OFF

	elif fan_id ==2 and status ==0 :	
		GPIO.setup(FAN2, GPIO.OUT)
		GPIO.output(FAN2, True)			#FAN 2 ON	

	elif fan_id ==2 and status ==1 :
		GPIO.setup(FAN2,GPIO.OUT)
		GPIO.output(FAN2, False)
	
	else: return HttpResponse("error")
	html= "fan " + str(fan_id) + " " + str(status)
	return HttpResponse(html)

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
	fan_status = Fan.objects.all()
	return HttpResponse(fan_status)

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
'''
def turnon(request):
	gpio.output(4,True)
	html= "Light is on"
	return HttpResponse(html)
			

def turnoff(request):
	gpio.output(4,False)
	html= "Light is off"
	return HttpResponse(html)

		
def led2(request):
	gpio.output(17,True)
	html= "Light 2 on"
	return HttpResponse(html)
def led2off(request):
	gpio.output(17,False)
	html= "Light 2 off"
	return HttpResponse(html)
'''
