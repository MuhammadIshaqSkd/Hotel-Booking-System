# Generated by Django 3.1.6 on 2021-02-20 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='state',
        ),
    ]