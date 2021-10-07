from django.db import models


# Create your models here.
class PenceramahModel(models.Model):
    penceramah = models.CharField(max_length=100)

    def __str__(self):
        return self.penceramah

class ImamModel(models.Model):
    nama = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='static/ustad/')

    def __str__(self):
        return self.nama


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
    link = models.CharField(default = "https://www.google.com", max_length=50)

    def __str__(self):
        return str(self.tanggal) + ' | ' + self.nama

class ZakatModel(models.Model):
    tanggal = models.DateField(auto_now_add=False)
    nama = models.CharField(max_length=100)
    total = models.IntegerField()
    link = models.CharField(default = "https://www.google.com", max_length=50)

    def __str__(self):
        return str(self.tanggal) + ' | ' + self.nama + ' | ' + str(self.jenis)

class ShodaqohModel(models.Model):
    tanggal = models.DateField(auto_now_add=False)
    nama = models.CharField(max_length=100)
    total = models.IntegerField()
    link = models.CharField(default = "https://www.google.com", max_length=50)

    def __str__(self):
        return str(self.tanggal) + ' | ' + self.nama + ' | ' + str(self.jenis)

class DonasiModel(models.Model):
    tanggal = models.DateField(auto_now_add=False)
    jumlah = models.IntegerField()
    nama = models.CharField(max_length=100)
    link = models.CharField(default = "https://www.google.com", max_length=50)

    def __str__(self):
        return str(self.tanggal) + ' | ' + self.nama

class WakafModel(models.Model):
    tanggal = models.DateField(auto_now_add=False)
    jumlah = models.IntegerField()
    nama = models.CharField(max_length=100)
    link = models.CharField(default = "https://www.google.com", max_length=50)

    def __str__(self):
        return str(self.tanggal) + ' | ' + self.nama

class KegiatanModel(models.Model):
    kegiatan = models.CharField(max_length=200)
    tanggal_kegiatan = models.DateField(auto_now=False, auto_now_add=False)
    deskripsi = models.TextField()
    thumbnail = models.ImageField(upload_to='static/thumbnail/')
    link = models.CharField(max_length=500, default='https://www.google.com/')
    upload = models.DateField(auto_now=True, editable=False)

    def __str__(self):
        return self.kegiatan  + ' | uploaded: ' + str(self.upload)

class LayananModel(models.Model):
    nama = models.CharField(max_length=20)
    nama_pengurus = models.CharField(max_length=50, default = 'Nama')
    no_telp = models.CharField(max_length=12)
    thumbnail = models.ImageField(upload_to='static/thumbnail_layanan/')

    def __str__(self):
        return self.nama + ' | ' + str(self.no_telp)

class JadwalJumatModel(models.Model):
    """Model definition for JadwalJumatModel."""

    # TODO: Define fields here
    tanggal = models.DateField(auto_now=False, auto_now_add=False)
    khatib = models.CharField( max_length=100)
    imam = models.CharField( max_length=100)
    muadzin = models.CharField( max_length=100)
    class Meta:
        """Meta definition for JadwalJumatModel."""

        verbose_name = 'Jadwal Jumat'
        verbose_name_plural = 'Jadwal Jumat'

    def __str__(self):
        """Unicode representation of JadwalJumatModel."""
        return str(self.tanggal)
