from django.db import models
import uuid
from . custom import generate_unique_random_numbers
import datetime
import accounts.models
# from .views import request
# Create your models here.

# complaintChoices = [
#     'Price Query',
#     'Driver Etiquette',
#     'Bad Customer Service',
#     'Car Cleanliness',
#     'Other'
# ]

class ComplaintForm(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ComplintId = models.CharField(max_length = 10, null = True, default = generate_unique_random_numbers(8))
    userName = models.CharField(max_length=100, blank=False, default=None)
    dateOfJourney = models.DateField(blank=False)
    phoneNumber = models.CharField(blank=False, max_length=20)
    pickUpAddress = models.TextField(blank=False)
    dropAddress = models.TextField(blank=False)
    complaintRegarding = models.TextField(blank=False)
    description = models.TextField(blank=False)
    opened = models.BooleanField(default=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.userName + '  -------  ' +str(self.id)



# Driver Details
class DriverFiles(models.Model):
    id = models.UUIDField(primary_key = True, editable = False, default = uuid.uuid4)
    driver_id = models.ForeignKey(accounts.models.CustomUser, on_delete = models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile/')
    DVLA_Driving_Licence = models.FileField(upload_to='DVLA/')
    DVLA_Check_Code = models.CharField(max_length = 20, null=True)
    Private_Hire_Driver_Badge = models.FileField(upload_to='driver_badge/')
    Private_Hire_Driver_Licence = models.FileField(upload_to='driver_Licence')
    Private_Hire_Vehicla_Licence = models.FileField(upload_to='vehicle_licence/')
    MOT_Test_Certificate = models.FileField(upload_to='MOT/')
    Vehicle_Insurance_Certificate = models.FileField(upload_to='Insurence/')
    V5C_LogBook_or_New_Keeper_Slip_or_E_LogBook = models.FileField(upload_to='logbook/')
    Bank_Statement = models.FileField(upload_to='bankstatement/')
    all_files_flag = models.BooleanField(default = False)
    time_stamp = models.DateTimeField(auto_now_add = True)
    accept_flag = models.BooleanField(default = False)