from django.db import models

# Create your models here.


class JadwalModel(models.Model):
    tanggal = models.DateTimeField(auto_now=False, auto_now_add=False)
    selesai = models.TimeField(
        auto_now=False, auto_now_add=False, default="23:00:00")
    title = models.CharField(max_length=100)
    penceramah = models.CharField(max_length=100)
    online = models.BooleanField()

    def __str__(self):
        return self.title + ' | ' + self.penceramah
