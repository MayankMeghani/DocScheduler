# Generated by Django 4.2.11 on 2024-03-06 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_alter_person_options_alter_person_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={},
        ),
        migrations.AlterModelTable(
            name='person',
            table='person',
        ),
    ]
