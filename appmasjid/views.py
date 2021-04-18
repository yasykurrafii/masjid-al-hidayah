from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home.html')

def jadwal(request):
    return render(request, 'jadwal.html')
    
def laporan(request):
    return render(request, 'laporan.html')

def informasi(request):
    return render(request, 'informasi.html')
