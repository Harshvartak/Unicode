from django.db import models

class spaceClass(models.Model):
	flight_number=models.IntegerField(primary_key=True)
	rocket_name=models.CharField(max_length=150)
	mission_patch=models.CharField(max_length=150,null=True)
	launch_time=models.DateTimeField(null=True)