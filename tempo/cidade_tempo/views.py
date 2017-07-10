# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import urllib2
import json

# Create your views here.


def index(request):
    saida = 'Consulta /tempo?q=nomeDacidade'
    return render(request, 'cidade_tempo/index.html', {'home': saida})

# Como parte da url
'''def tempo(request, cidade):
    return render(request, 'cidade_tempo/index.html', {'home': cidade})'''


def tempo(request):
    city = request.GET.get('cidade');

    if city != None:
        url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID=8c9ca0dfddb5f4e3074aaee1dc85b045"
        req = urllib2.urlopen(url).read()
        saida = json.loads(req)
        home = 'Cidade: ' + city + ' Temp: ' + str(saida['main']['temp']) + ' °f'
        return render(request, 'cidade_tempo/index.html', {'home': home})
    else:
        return render(request, 'cidade_tempo/index.html', {'home': 'Cidade não fornecida'})