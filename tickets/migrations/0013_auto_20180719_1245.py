# Generated by Django 2.0 on 2018-07-19 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0012_auto_20180719_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 19, 12, 45, 7, 702057), verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='dataAbertura',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 19, 12, 45, 7, 701476), verbose_name='Data de Abertura'),
        ),
    ]
