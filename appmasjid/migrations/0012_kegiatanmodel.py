# Generated by Django 3.1.4 on 2021-05-20 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmasjid', '0011_jadwalmodel_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='KegiatanModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kegiatan', models.CharField(max_length=200)),
                ('tanggal_kegiatan', models.DateField()),
                ('deskripsi', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='thumbnail/')),
            ],
        ),
    ]
