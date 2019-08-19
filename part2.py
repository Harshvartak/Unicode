import requests
import json
import time
url = 'https://api.spacexdata.com/v3/launches'


response=requests.get(url)
res=response.json()

final=[]

for i in res:
    di={}
    di={'flight number':i['flight_number'],'rocket name':i['rocket']['rocket_name'],'launch date':time.strftime("%D %H:%M", time.localtime(i['launch_date_unix'])),'mission patch link':i['links']['mission_patch']}
    final.append(di)


print(final) 


