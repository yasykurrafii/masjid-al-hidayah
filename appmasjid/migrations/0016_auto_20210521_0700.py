# Generated by Django 3.1.4 on 2021-05-21 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmasjid', '0015_kegiatanmodel_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kegiatanmodel',
            name='thumbnail',
            field=models.ImageField(upload_to='static/thumbnail/'),
        ),
    ]