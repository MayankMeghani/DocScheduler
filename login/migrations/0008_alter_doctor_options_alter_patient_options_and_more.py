# Generated by Django 4.2.11 on 2024-03-06 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_alter_person_options_alter_person_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={},
        ),
        migrations.AlterModelTable(
            name='doctor',
            table='doctor',
        ),
        migrations.AlterModelTable(
            name='patient',
            table='patient',
        ),
    ]
