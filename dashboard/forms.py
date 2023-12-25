from django.forms import ModelForm
from . models import airportCity, Fleet


class MyAirportCity(ModelForm):
    class Meta:
        model = airportCity
        exclude = ('id', 'fromCity')

class MyFleets(ModelForm):
    class Meta:
        model = Fleet
        fields = '__all__'