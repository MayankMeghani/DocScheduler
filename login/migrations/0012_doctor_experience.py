# Generated by Django 4.2.11 on 2024-03-10 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_person_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='experience',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
