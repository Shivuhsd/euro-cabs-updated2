# Generated by Django 5.0 on 2023-12-14 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_businessform_alter_airportcity_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessform',
            name='contactName',
        ),
    ]