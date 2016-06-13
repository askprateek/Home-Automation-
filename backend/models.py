from django.db import models

class Led(models.Model):
	led_id = models.PositiveSmallIntegerField()
	status = models.BooleanField(default =0)
	
	
class Fan(models.Model):
	fan_id = models.PositiveSmallIntegerField()	
	status = models.BooleanField(default =0)
	


