# Generated by Django 2.0.5 on 2018-05-18 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['titulo', 'descricao'], 'verbose_name': 'Ticket', 'verbose_name_plural': 'Tickets'},
        ),
        migrations.AlterField(
            model_name='ticket',
            name='descricao',
            field=models.TextField(max_length=2000, verbose_name='Descrição'),
        ),
    ]