from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('laporan/', views.laporan, name='laporan'),
    path('jadwal/', views.jadwal, name='jadwal'),
    path('informasi/', views.informasi, name='informasi'),
]
