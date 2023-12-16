from django.db import models
import uuid
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
    userName = models.CharField(max_length=100, blank=False, default=None)
    dateOfJourney = models.DateField(blank=False)
    phoneNumber = models.CharField(blank=False, max_length=20)
    pickUpAddress = models.TextField(blank=False)
    dropAddress = models.TextField(blank=False)
    complaintRegarding = models.TextField(blank=False)
    description = models.TextField(blank=False)
    opened = models.BooleanField(default=False, blank=False)


    def __str__(self):
        return self.userName + '  -------  ' +str(self.id)



