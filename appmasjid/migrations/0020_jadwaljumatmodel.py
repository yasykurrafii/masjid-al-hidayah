# Generated by Django 3.1.4 on 2021-05-31 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmasjid', '0019_imammodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='JadwalJumatModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField()),
                ('khatib', models.CharField(max_length=100)),
                ('imam', models.CharField(max_length=100)),
                ('muadzin', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Jadwal Jumat',
                'verbose_name_plural': 'Jadwal Jumat',
            },
        ),
    ]