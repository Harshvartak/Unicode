# Generated by Django 2.2.3 on 2019-08-22 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacex', '0004_auto_20190822_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='flight_number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]