# Generated by Django 3.1.4 on 2021-10-20 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmasjid', '0022_auto_20211007_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donasimodel',
            name='link',
            field=models.CharField(default='https://www.google.com', max_length=1000),
        ),
        migrations.AlterField(
            model_name='infaqmodel',
            name='link',
            field=models.CharField(default='https://www.google.com', max_length=1000),
        ),
        migrations.AlterField(
            model_name='shodaqohmodel',
            name='link',
            field=models.CharField(default='https://www.google.com', max_length=1000),
        ),
        migrations.AlterField(
            model_name='wakafmodel',
            name='link',
            field=models.CharField(default='https://www.google.com', max_length=1000),
        ),
        migrations.AlterField(
            model_name='zakatmodel',
            name='link',
            field=models.CharField(default='https://www.google.com', max_length=1000),
        ),
    ]