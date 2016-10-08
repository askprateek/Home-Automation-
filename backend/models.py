from django.db import models

class Led(models.Model):
	led_id = models.PositiveSmallIntegerField()
	status = models.BooleanField(default =0)
	
	
class Fan(models.Model):
	fan_id = models.PositiveSmallIntegerField()	
	status = models.BooleanField(default =0)

class Device(models.Model):
	type = models.CharField(max_length=10)
	device_id = models.PositiveSmallIntegerField()
	status = models.BooleanField(default =0)
	pin_no = models.PositiveSmallIntegerField()

	def __str__(self):
		return str(self.type.capitalize()) + " " + str(self.device_id) + " " + str(self.status) + " Pin: " + str(self.pin_no)


