# Generated by Django 4.2.11 on 2024-03-11 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_rename_doctor_id_appointment_doctor_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.CharField(max_length=20),
        ),
    ]