# Generated by Django 3.1.4 on 2021-05-12 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmasjid', '0006_auto_20210512_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donasimodel',
            name='tanggal',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='infaqmodel',
            name='tanggal',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='shodaqohmodel',
            name='tanggal',
            field=models.DateField(),
        ),
    ]
