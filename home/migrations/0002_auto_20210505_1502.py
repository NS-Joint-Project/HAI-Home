# Generated by Django 3.2 on 2021-05-05 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timemodel',
            name='departure_time',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='timemodel',
            name='return_time',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
