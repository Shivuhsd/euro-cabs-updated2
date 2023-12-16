from django.urls import path
from . import views

urlpatterns = [
#     path('/', views.adminDashborad, name='adminDashboard'),
    #Complaint Endpoint
    path('home/', views.home, name='home'),
    path('privacyAndPolicy/', views.privacyAndPolicy, name='privacyPolicy'),
    path('rides/', views.rides, name='rides'),
    path('websiteTerms/', views.websiteTerms, name='websiteTerms'),
    path('corporate/', views.corporate, name='corporate'),
    path('businessT&C/', views.businessTerms, name='businessTerms'),
    path('driverRegister/', views.driverRegister, name='driverRegister'),
    path('complaintForm/', views.complaintForm, name='complaintForm'),
    path('businessForm/', views.businessForm, name='businessForm'),
    path('airportDest/', views.airportDest, name='airportDest'),
]