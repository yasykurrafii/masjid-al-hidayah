from django.shortcuts import render
import datetime
from .models import *

# Create your views here.
date = datetime.datetime.now()
date = date.strftime("%A, %d %B %Y")
def index(request):
    jadwal = JadwalModel.objects.all()
    return render(request, 'home.html', {'date': date, 'jadwal': jadwal})

def jadwal(request):
    return render(request, 'jadwal.html', {'date': date})
    
def laporan(request):
    return render(request, 'laporan.html', {'date': date})

def informasi(request):
    return render(request, 'informasi.html', {'date': date})
