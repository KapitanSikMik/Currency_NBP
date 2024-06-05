# Generated by Django 5.0.6 on 2024-06-04 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('rate', models.DecimalField(decimal_places=8, max_digits=15, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
