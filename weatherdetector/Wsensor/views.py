from django.shortcuts import render
import json
import urllib.request


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=f49b112bedc14792423e739179e5ee88').read()
        json_data = json.loads(res)
        data ={
            'country' : str(json_data['sys']['country']),
            'coordinate': str(f"{json_data['coord']['lon']} {json_data['coord']['lat']}"),
            'temp': str(json_data['main']['temp']) + 'K',
            'pressure': str(json_data['main']['pressure']),
            'humidity' : str(json_data['main']['humidity']),
        }

        context ={
            'data':data,
            'city': city
        }
    
    else:
        data = {}


    return render(request, 'index.html', context)
