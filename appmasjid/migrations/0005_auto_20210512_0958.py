# Generated by Django 3.1.4 on 2021-05-12 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appmasjid', '0004_donasimodel_jenisshodaqoh_shodaqohmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shodaqohmodel',
            name='jenis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appmasjid.jenisshodaqoh'),
        ),
    ]
