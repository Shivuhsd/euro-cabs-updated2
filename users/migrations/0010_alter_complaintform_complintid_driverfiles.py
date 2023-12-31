# Generated by Django 5.0 on 2023-12-24 10:15

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_complaintform_complintid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintform',
            name='ComplintId',
            field=models.CharField(default='CM63125074', max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='DriverFiles',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('DVLA_Driving_Licence', models.FileField(upload_to='DVLA/')),
                ('DVLA_Check_Code', models.CharField(max_length=20, null=True)),
                ('Private_Hire_Driver_Badge', models.FileField(upload_to='driver_badge/')),
                ('Private_Hire_Driver_Licence', models.FileField(upload_to='driver_Licence')),
                ('Private_Hire_Vehicla_Licence', models.FileField(upload_to='vehicle_licence/')),
                ('MOT_Test_Certificate', models.FileField(upload_to='MOT/')),
                ('Vehicle_Insurance_Certificate', models.FileField(upload_to='Insurence/')),
                ('V5C_LogBook_or_New_Keeper_Slip_or_E_LogBook', models.FileField(upload_to='logbook/')),
                ('Bank_Statement', models.FileField(upload_to='bankstatement/')),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
