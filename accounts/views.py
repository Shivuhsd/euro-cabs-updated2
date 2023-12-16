from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.

# Fuction to Login the User Using Email and Password

def userLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email = email, password = password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                print("True")
                return redirect('adminDashboard')
            else:
                print("The User Will Be Redirected to User Dashborad.....")
        else:
            print("Check Your Credentials...")
    return render(request, 'auth/login.html')

# Function to Logout the User

def userLogout(request):
    logout(request)
    return redirect('userLogin')

# def adminLogin(request):
#     return render(request, 'auth/adminlogin.html')

