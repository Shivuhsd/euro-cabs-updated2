from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminDashborad, name='adminDashboard'),
    path('complaints/', views.complaints, name='complaints'),
    path('<str:pk>/showComplaint/', views.showComplaint, name='showComplaint'),
    path('<str:pk>/tokenAccepted/', views.tokenAccepted, name='tokenAccepted'),
    path('addAirports/', views.addAirports, name='addAirports'),
    path('<str:pk>/manage/', views.cityManage, name='cityManage'),
    path('<str:pk>/editCity/', views.editCity, name='editCity'),
    path('<str:pk>/deleteCity/', views.deleteCity, name='deleteCity'),
    path('<str:pk>/deleteAirport/', views.deleteAirport, name='deleteAirport'),
]