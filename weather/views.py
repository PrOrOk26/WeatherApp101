from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms.WeatherDataForm import WeatherDataForm
from .scrapper.WeatherScrapper import WeatherScrapper


def index(request):
    if request.method == 'POST':
        weather_form = WeatherDataForm(request.POST)
        if weather_form.is_valid():
            return HttpResponseRedirect(reverse('weather', kwargs={'city_name': request.POST.get('city')}))
    else:
        weather_form = WeatherDataForm()
    return render(request, 'weather/main.html', {'weather_form': weather_form})


def weather(request, city_name):
    city_weather = WeatherScrapper.get_weather(city_name=city_name,
                                               units='metric')
    return render(request, 'weather/weather_result.html',
                      {'city_weather': city_weather})

