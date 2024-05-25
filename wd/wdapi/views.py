import os
from django.shortcuts import render
from django.http import HttpResponse
import requests
from .forms import LocationForm

def api_view(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            api_url = f'https://api.api-ninjas.com/v1/weather?city={city}'
            response = requests.get(api_url, headers={'X-Api-Key': os.environ.get('API_KEY')})
            if response.status_code == 200:
                weather_data = response.json()
                return render(request, 'wdapi/index.html', {'weather': weather_data, 'form': form})
            else:
                return HttpResponse(f"Error: {response.status_code} {response.text}", status=response.status_code)
    else:
        form = LocationForm()
    
    return render(request, 'wdapi/index.html', {'form': form})
