# Generated by Django 4.2.11 on 2024-03-30 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0006_appointment_issue_alter_appointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='issue',
            field=models.CharField(max_length=500),
        ),
    ]