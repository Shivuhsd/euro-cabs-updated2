# Generated by Django 5.0 on 2023-12-26 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_complaintform_complintid_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaintform',
            name='mail',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
