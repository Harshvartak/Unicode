from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
import time
from django.template.loader import render_to_string
from .models import spaceClass
from . import models 


def spaceX(request):
	connect=requests.get('https://api.spacexdata.com/v3/launches')
	result=connect.json()

	for i in result:
		#addition of data from data base after importing it ny API with JSON
		space=models.spaceClass()
		space.flight_number=i['flight_number']
		space.rocket_name=i['rocket']['rocket_name']
		#date object made compatible for model
		space.launch_date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i['launch_date_unix']))
		space.mission_patch=i['links']['mission_patch']
		space.save()


		data={"final":spaceClass.objects.all()}
		ren=render_to_string('SoaceX/final.html',data)

	return HttpResponse(ren)	

