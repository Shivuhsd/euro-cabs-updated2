# Generated by Django 5.0 on 2023-12-24 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_complaintform_complintid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintform',
            name='ComplintId',
            field=models.CharField(default='CM73264510', max_length=10, null=True),
        ),
    ]
