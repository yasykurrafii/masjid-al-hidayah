from django.shortcuts import render
import datetime
import requests
from .models import *

# Create your views here.

# Global Variable untuk date
date = datetime.datetime.now()
now = date.strftime("%A, %d %B %Y")

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
    jadwal = JadwalModel.objects.all()[:5]
    return render(request, 'home.html', {'date': now,
                                         'jadwal': jadwal,
                                         'subuh': solat['Fajr'],
                                         'dzuhur': solat['Dhuhr'],
                                         'ashr': solat['Asr'],
                                         'maghrib': solat['Maghrib'],
                                         'isya': solat['Isha']})


def jadwal(request):
    solat = fetch_solat()
    solat = solat['results']['datetime'][0]['times']
    bulanIni = datetime.date(date.year, date.month, date.day)
    if int(date.month) == 12:
        bulanDepan = datetime.date(
            int(date.year) + 1, (int(date.month) % 12) + 1, date.day)
    else:
        bulanDepan = datetime.date(date.year, int(date.month) + 1, date.day)
    dateLalu = datetime.date(date.year, 1,1)
    jadwalBulanIni = JadwalModel.objects.filter(
        tanggal__range=[bulanIni, bulanDepan]).order_by('-tanggal')
    jadwalLewat = JadwalModel.objects.filter(tanggal__range=[dateLalu,bulanIni])[:5]
    return render(request, 'jadwal.html', {'date': now, 'subuh': solat['Fajr'],
                                           'dzuhur': solat['Dhuhr'],
                                           'ashr': solat['Asr'],
                                           'maghrib': solat['Maghrib'],
                                           'isya': solat['Isha'],
                                           'jadwal': jadwalBulanIni,
                                           'jadwalLewat':jadwalLewat})


def laporan(request):
    solat = fetch_solat()
    solat = solat['results']['datetime'][0]['times']
    return render(request, 'laporan.html', {'date': now, 'subuh': solat['Fajr'],
                                            'dzuhur': solat['Dhuhr'],
                                            'ashr': solat['Asr'],
                                            'maghrib': solat['Maghrib'],
                                            'isya': solat['Isha']})


def informasi(request):
    solat = fetch_solat()
    solat = solat['results']['datetime'][0]['times']
    return render(request, 'informasi.html', {'date': now, 'subuh': solat['Fajr'],
                                              'dzuhur': solat['Dhuhr'],
                                              'ashr': solat['Asr'],
                                              'maghrib': solat['Maghrib'],
                                              'isya': solat['Isha']})
