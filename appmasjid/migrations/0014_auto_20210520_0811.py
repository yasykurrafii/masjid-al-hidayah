# Generated by Django 3.1.4 on 2021-05-20 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmasjid', '0013_auto_20210520_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='kegiatanmodel',
            name='link',
            field=models.CharField(default='https://www.google.com/', max_length=500),
        ),
        migrations.AlterField(
            model_name='kegiatanmodel',
            name='thumbnail',
            field=models.ImageField(upload_to='thumbnail/%Y/%m/%d/'),
        ),
    ]
