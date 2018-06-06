# Generated by Django 2.0.5 on 2018-06-06 12:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0009_auto_20180605_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(max_length=1000, verbose_name='Texto')),
                ('data', models.DateTimeField(default=datetime.datetime(2018, 6, 6, 12, 55, 30, 167345), verbose_name='Data')),
            ],
        ),
        migrations.AlterField(
            model_name='ticket',
            name='dataAbertura',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 6, 12, 55, 30, 166857), verbose_name='Data de Abertura'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Ticket'),
        ),
    ]
