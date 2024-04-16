from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
import json
import urllib.request

# Create your views here.
def weather(request):
  if(request.method == 'POST'):
    city = request.POST['city']

    #Here you see url. After "appid=", the string is the API key for the weather. You can get key that from https://home.openweathermap.org/api_keys
    source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=5f6a814e16b63c0b748bd0c49f7ba5b0').read()
    
    list_of_data = json.loads(source)

    
    data = {
      "country_code": str(list_of_data['sys']['country']), 
      "coordinate": str(list_of_data['coord']['lon']) + ' '
                  + str(list_of_data['coord']['lat']), 
      "temp": str(list_of_data['main']['temp']) + 'k', 
      "pressure": str(list_of_data['main']['pressure']), 
      "humidity": str(list_of_data['main']['humidity']),
    }
    #You can see the data of list_of_data
    # print(list_of_data)
  else:
    data = {}
  return render(request, 'climate/weather.html', data)