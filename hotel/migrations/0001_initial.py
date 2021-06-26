# Generated by Django 3.1.6 on 2021-02-13 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=50)),
                ('vprp', models.IntegerField(default=0)),
                ('grp', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='hotel/images')),
                ('vpr_img', models.ImageField(default='', upload_to='hotel/images')),
                ('gr_img', models.ImageField(default='', upload_to='hotel/images')),
            ],
        ),
    ]
