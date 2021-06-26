# Generated by Django 3.1.6 on 2021-02-19 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('amount', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=111)),
                ('address', models.CharField(max_length=111)),
                ('city', models.CharField(max_length=111)),
                ('state', models.CharField(max_length=111)),
                ('zip_code', models.CharField(max_length=111)),
                ('phone', models.CharField(default='', max_length=111)),
                ('hotel_name', models.CharField(max_length=90)),
                ('room_type', models.CharField(max_length=90)),
                ('No_room', models.CharField(default='', max_length=111)),
            ],
        ),
    ]
