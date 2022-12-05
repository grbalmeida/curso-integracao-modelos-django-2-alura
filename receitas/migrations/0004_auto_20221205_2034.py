# Generated by Django 3.0.14 on 2022-12-05 23:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0003_auto_20221205_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 5, 20, 34, 44, 908881)),
        ),
    ]