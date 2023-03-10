# Generated by Django 4.1.5 on 2023-02-04 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0005_remove_reservation_time_log_reservation_booking_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
    ]
