from django.db import models

class Device(models.Model):
	name = models.CharField(max_length=20)
	type = models.CharField(max_length=20)
	device_id = models.AutoField(primary_key = True)
	status = models.BooleanField(default =0)
	pin_no = models.PositiveSmallIntegerField()
	#id = models.CharField(max_length=50)
	#url = models.CharField(max_length=50)
	room = models.ForeignKey('backend.Room')


	def __str__(self):
		return str(self.name.capitalize()) + " " + str(self.device_id) + " " + str(self.status) + " Pin: " + str(self.pin_no)

class Room(models.Model):
	name = models.CharField(max_length = 20)
	
	def __str__(self):
		return str(self.name)
	

