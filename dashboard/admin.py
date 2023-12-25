from django.contrib import admin
from .models import airportRates, airportCity, businessForm, Fleet

# Register your models here.

admin.site.register(airportRates)
admin.site.register(airportCity)
admin.site.register(businessForm)
admin.site.register(Fleet)
