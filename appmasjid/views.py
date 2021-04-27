from django.shortcuts import render
import datetime
import requests
from .models import *

# Create your views here.

# Global Variable untuk date
date = datetime.datetime.now()
date = date.strftime("%A, %d %B %Y")

# Function untuk fetching api


def fetch_solat():
    tanggal = datetime.datetime.now()
    tanggal = tanggal.strftime("%Y-%m-%d")
    data = requests.get(
        "https://api.pray.zone/v2/times/day.json?city=jakarta&date=" + tanggal)
    return data.json()

# Function render


def index(request):
    solat = fetch_solat()
    solat = solat['results']['datetime'][0]['times']
    jadwal = JadwalModel.objects.all()
    return render(request, 'home.html', {'date': date,
                                         'jadwal': jadwal,
                                         'subuh': solat['Fajr'],
                                         'dzuhur': solat['Dhuhr'],
                                         'ashr': solat['Asr'],
                                         'maghrib': solat['Maghrib'],
                                         'isya': solat['Isha']})


def jadwal(request):
    solat = fetch_solat()
    solat = solat['results']['datetime'][0]['times']
    return render(request, 'jadwal.html', {'date': date, 'subuh': solat['Fajr'],
                                           'dzuhur': solat['Dhuhr'],
                                           'ashr': solat['Asr'],
                                           'maghrib': solat['Maghrib'],
                                           'isya': solat['Isha']})


def laporan(request):
    solat = fetch_solat()
    solat = solat['results']['datetime'][0]['times']
    return render(request, 'laporan.html', {'date': date, 'subuh': solat['Fajr'],
                                            'dzuhur': solat['Dhuhr'],
                                            'ashr': solat['Asr'],
                                            'maghrib': solat['Maghrib'],
                                            'isya': solat['Isha']})


def informasi(request):
    solat = fetch_solat()
    solat = solat['results']['datetime'][0]['times']
    return render(request, 'informasi.html', {'date': date, 'subuh': solat['Fajr'],
                                              'dzuhur': solat['Dhuhr'],
                                              'ashr': solat['Asr'],
                                              'maghrib': solat['Maghrib'],
                                              'isya': solat['Isha']})
