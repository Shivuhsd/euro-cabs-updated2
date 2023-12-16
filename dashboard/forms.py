from django.forms import ModelForm
from . models import airportCity


class MyAirportCity(ModelForm):
    class Meta:
        model = airportCity
        exclude = ('id', 'fromCity')