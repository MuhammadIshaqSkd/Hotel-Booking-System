# Generated by Django 3.1.6 on 2021-02-20 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_bookingupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingupdate',
            name='room_no',
            field=models.CharField(default='', max_length=5000),
        ),
    ]