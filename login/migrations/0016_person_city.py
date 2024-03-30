# Generated by Django 4.2.11 on 2024-03-30 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_person_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='city',
            field=models.CharField(choices=[('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Bangalore', 'Bangalore'), ('Hyderabad', 'Hyderabad'), ('Ahmedabad', 'Ahmedabad'), ('Chennai', 'Chennai'), ('Kolkata', 'Kolkata'), ('Surat', 'Surat'), ('Pune', 'Pune'), ('Jaipur', 'Jaipur'), ('Nadiad', 'Nadiad')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
