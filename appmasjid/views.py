from django.shortcuts import render
from django.utils import timezone
from django.db.models import Sum
import datetime
import requests
from .models import *

# Create your views here.

# Global Variable untuk date
date = timezone.now()
now = date.strftime("%A, %d %B %Y")

# Function untuk fetching api


def fetch_solat():
    tanggal = timezone.now()
    tanggal = tanggal.strftime("%Y-%m-%d")
    data = requests.get(
        "https://api.pray.zone/v2/times/day.json?city=jakarta&date=" + tanggal)
    return data.json()

# Function render


def index(request):
    solat = fetch_solat()
    solat = solat['results']['datetime'][0]['times']
    jadwal = JadwalModel.objects.all().order_by('-id')[:5]
    infaq = InfaqModel.objects.aggregate(Sum('jumlah'))
    zakat = ZakatModel.objects.aggregate(Sum('total'))
    wakaf = WakafModel.objects.aggregate(Sum('jumlah'))
    donasi = DonasiModel.objects.aggregate(Sum('jumlah'))
    shodaqoh = ShodaqohModel.objects.aggregate(Sum('total'))
    layanan = LayananModel.objects.all()
    kegiatan = KegiatanModel.objects.all()
    jumat = JadwalJumatModel.objects.all().order_by('-id')[:5]
    return render(request, 'home.html', {'date': now,
                                         'jadwal': jadwal,
                                         'subuh': solat['Fajr'],
                                         'dzuhur': solat['Dhuhr'],
                                         'ashr': solat['Asr'],
                                         'maghrib': solat['Maghrib'],
                                         'isya': solat['Isha'],
                                         'navhome' : 'active',
                                         'infaq': infaq,'zakat': zakat,'wakaf': wakaf,'donasi': donasi,'shodaqoh': shodaqoh,
                                         'kegiatan': kegiatan,
                                         'layanan' : layanan,
                                         'jumat':jumat})


def jadwal(request):
    solat = fetch_solat()
    solat = solat['results']['datetime'][0]['times']
    bulanIni = datetime.date(date.year, date.month, date.day)
    bulanDepan = datetime.date(date.year, 1,1)
    if int(date.month) == 12:
        bulanDepan = datetime.date(
            int(date.year) + 1, (int(date.month) % 12) + 1, date.day)
    elif int(date.month) == 2:
        if int(date.year)%4 == 0:
            bulanDepan = datetime.date(
                int(date.year) + 1, (int(date.month) % 12) + 1, date.day-2)
        else:
            bulanDepan = datetime.date(
                int(date.year) + 1, (int(date.month) % 12) + 1, date.day-3)
    elif int(date.month)%2 == 0:
        bulanDepan = datetime.date(
                int(date.year) + 1, (int(date.month) % 12) + 1, date.day-1)
    dateLalu = datetime.date(date.year, 1,1)
    jadwalBulanIni = JadwalModel.objects.filter(
        tanggal__range=[bulanIni, bulanDepan]).order_by('tanggal')
    jadwalLewat = JadwalModel.objects.filter(tanggal__range=[dateLalu,bulanIni])[:5]
    jumat = JadwalJumatModel.objects.all()[:5]
    return render(request, 'jadwal.html', {'date': now, 'subuh': solat['Fajr'],
                                           'dzuhur': solat['Dhuhr'],
                                           'ashr': solat['Asr'],
                                           'maghrib': solat['Maghrib'],
                                           'isya': solat['Isha'],
                                           'jadwal': jadwalBulanIni,
                                           'jadwalLewat':jadwalLewat,
                                           'navjadwal' : 'active',
                                           'jumat':jumat})


def laporan(request):
    solat = fetch_solat()
    solat = solat['results']['datetime'][0]['times']
    infaq = InfaqModel.objects.all()
    zakat = ZakatModel.objects.all()
    wakaf = WakafModel.objects.all()
    shodaqoh = ShodaqohModel.objects.all()
    donasi = DonasiModel.objects.all()
    return render(request, 'laporan.html', {'date': now, 'subuh': solat['Fajr'],
                                            'dzuhur': solat['Dhuhr'],
                                            'ashr': solat['Asr'],
                                            'maghrib': solat['Maghrib'],
                                            'isya': solat['Isha'],
                                            'navlaporan' : 'active',
                                            'infaq': infaq, 'zakat':zakat,
                                            'wakaf':wakaf,'shodaqoh':shodaqoh,
                                            'donasi':donasi})


def informasi(request):
    solat = fetch_solat()
    solat = solat['results']['datetime'][0]['times']
    imam = ImamModel.objects.all()
    return render(request, 'informasi.html', {'date': now, 'subuh': solat['Fajr'],
                                              'dzuhur': solat['Dhuhr'],
                                              'ashr': solat['Asr'],
                                              'maghrib': solat['Maghrib'],
                                              'isya': solat['Isha'],
                                              'navinformasi' : 'active',
                                              'imam' : imam})
