# Generated by Django 2.1.7 on 2019-02-11 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('trip_id', models.AutoField(max_length=30, primary_key=True, serialize=False)),
                ('driver_name', models.CharField(max_length=50)),
                ('reg_number', models.CharField(max_length=15)),
                ('opening_milage', models.CharField(max_length=20)),
                ('closing_milage', models.IntegerField()),
                ('destination', models.IntegerField()),
                ('comments', models.TextField()),
                ('distance', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(max_length=15, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=256)),
            ],
        ),
    ]
