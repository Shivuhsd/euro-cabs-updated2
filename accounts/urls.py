from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.userLogin, name='userLogin'),
    path('userLogout/', views.userLogout, name='userLogout'),
   # path('adminlogin/', views.adminLogin, name='adminlogin'),
]
