# Generated by Django 3.1.4 on 2021-05-19 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appmasjid', '0007_auto_20210512_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shodaqohmodel',
            name='jenis',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appmasjid.jenisshodaqoh'),
        ),
    ]
