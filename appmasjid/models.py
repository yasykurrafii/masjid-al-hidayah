from django.db import models

# Create your models here.
class PenceramahModel(models.Model):
    penceramah = models.CharField(max_length=100)

    def __str__(self):
        return self.penceramah

class JenisZakatModel(models.Model):
    jenis = models.CharField(max_length=100)

    def __str__(self):
        return self.jenis

class JenisShodaqoh(models.Model):
    jenis = models.CharField(max_length=50)

    def __str__(self):
        return self.jenis

class JadwalModel(models.Model):
    tanggal = models.DateTimeField(auto_now=False, auto_now_add=False)
    selesai = models.TimeField(
        auto_now=False, auto_now_add=False, default="23:00:00")
    title = models.CharField(max_length=100)
    penceramah = models.ForeignKey(PenceramahModel, on_delete=models.CASCADE)
    online = models.BooleanField()
    link = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.penceramah)

class InfaqModel(models.Model):
    tanggal = models.DateField(auto_now_add=False)
    jumlah = models.IntegerField()
    nama = models.CharField(max_length=100)

    def __str__(self):
        return str(self.tanggal) + ' | ' + self.nama

class ZakatModel(models.Model):
    tanggal = models.DateField(auto_now_add=False)
    nama = models.CharField(max_length=100)
    total = models.IntegerField()
    jenis = models.ForeignKey(JenisZakatModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.tanggal) + ' | ' + self.nama + ' | ' + str(self.jenis)

class ShodaqohModel(models.Model):
    tanggal = models.DateField(auto_now_add=False)
    nama = models.CharField(max_length=100)
    total = models.IntegerField()
    jenis = models.ForeignKey(JenisShodaqoh, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.tanggal) + ' | ' + self.nama + ' | ' + str(self.jenis)

class DonasiModel(models.Model):
    tanggal = models.DateField(auto_now_add=False)
    jumlah = models.IntegerField()
    nama = models.CharField(max_length=100)

    def __str__(self):
        return str(self.tanggal) + ' | ' + self.nama

class WakafModel(models.Model):
    tanggal = models.DateField(auto_now_add=False)
    jumlah = models.IntegerField()
    nama = models.CharField(max_length=100)

    def __str__(self):
        return str(self.tanggal) + ' | ' + self.nama

class KegiatanModel(models.Model):
    kegiatan = models.CharField(max_length=200)
    tanggal_kegiatan = models.DateField(auto_now=False, auto_now_add=False)
    deskripsi = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnail/%Y/%m/%d/')
    link = models.CharField(max_length=500, default='https://www.google.com/')

    def __str__(self):
        return self.kegiatan + ' | ' + str(self.tanggal_kegiatan)