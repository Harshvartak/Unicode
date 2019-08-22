from django.shortcuts import render
import json
import requests
import time
from django.http import HttpResponse


def spaceX(request):
	url = 'https://api.spacexdata.com/v3/launches'


	response=requests.get(url)
	res=response.json()

	final=[]

	for i in res:
		di={}
		di={'flight_number':i['flight_number'],'rocket_name':i['rocket']['rocket_name'],'launch_date':time.strftime("%D %H:%M", time.localtime(i['launch_date_unix'])),'mission_patch':i['links']['mission_patch']}
		final.append(di)
	print(di)	




	return HttpResponse("<p><h2>{}</h2></p>" .format(i) for i in final)

