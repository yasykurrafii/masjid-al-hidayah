# Generated by Django 3.1.4 on 2021-04-27 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmasjid', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jadwalmodel',
            name='selesai',
            field=models.TimeField(default='23:00:00'),
        ),
    ]