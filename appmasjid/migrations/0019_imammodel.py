# Generated by Django 3.1.4 on 2021-05-21 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmasjid', '0018_delete_jeniszakatmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImamModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('foto', models.ImageField(upload_to='static/ustad/')),
            ],
        ),
    ]