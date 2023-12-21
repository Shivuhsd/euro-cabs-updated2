from django.shortcuts import render, redirect
from django.urls import reverse
import users.models
from . models import airportRates, airportCity, businessForm
from django.http import HttpResponse, JsonResponse
from .forms import MyAirportCity
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

# Fuction to Load Dashboard of the Admin
@login_required
def adminDashborad(request):
    if request.user.is_superuser:
        return render(request, 'admin/dashboard.html')
    return render(request, 'admin/notAuthorised.html')

# Function to Load the Complaints to the user

def complaints(request):
    if request.user.is_superuser:
        data = users.models.ComplaintForm.objects.all()

        context = {
            'complaints': data
        }
    else:
        return render(request, 'admin/notAuthorised.html')
    return render(request, 'admin/complaints.html', context)


# Function to Display the Complaint to Admin

def showComplaint(request, pk):
    if request.user.is_superuser:
        try:
            data = users.models.ComplaintForm.objects.get(id = pk)

            context = {
                'data': data
            }
            return render(request, 'admin/showComplaint.html', context)
        except:
            return custom404(request)
    else:
        return render(request, 'admin/notAuthorised.html')

#Function To Accept the Token

def tokenAccepted(request, pk):
    try:
        data = users.models.ComplaintForm.objects.get(id = pk)
        data.opened = True
        data.save()
        return JsonResponse({'status': 'success'})
    except:
        return JsonResponse({'status': 'failed'})
   

# Fucntion to Add Airports to the list

def addAirports(request):
    if request.user.is_superuser:
        data = airportRates.objects.all()
    
        if request.method == 'POST':
            airportName = request.POST['airportName']
            try:
                form = airportRates(airportName = airportName)
                form.save()
            except:
                print("Something Went Wrong")

        context = {
            'data': data
        }
        return render(request, 'admin/addAirport.html', context)
    else:
        return render(request, 'admin/notAuthorised.html')


# Function to Manage the City
    
def cityManage(request, pk):
    if request.user.is_superuser:
        form = MyAirportCity()
        aid = airportRates.objects.get(id = pk)
        data = airportCity.objects.filter(fromCity = pk)
        if request.method == 'POST':
            data = MyAirportCity(request.POST)
            if data.is_valid():
                obj = data.save(commit=False)
                obj.fromCity = aid
                obj.save()
                return redirect(reverse('cityManage', args = [pk]))
            else:
                messages.error("Something Went Wrong...")
                # print("Some Thing is Wrong in your data")
        # cityName = request.POST['cityName']
        # day = request.POST['day']
        # night = request.POST['night']
        # form = airportCity(fromCity = aid, to = cityName, dayRate = day, nightRate = night)
        # try:
        #     form.save()
        # except:
        #     print("Something Went Wrong..")
        context = {
            'data': data,
            'form': form,
            'aid': aid
        }
        return render(request, 'admin/cityManage.html', context)
    else:
        return render(request, 'admin/notAuthorised.html')


# Custom View for 404(Page Not Found)

def custom404(request, exception = None):
    return render(request, 'admin/404.html', status=404)



# Function to Edit the City

def editCity(request, pk):
    if request.user.is_superuser:

        data = airportCity.objects.get(id = pk)
        form = MyAirportCity(instance=data)
        aid = airportRates.objects.get(id = data.fromCity.id)

        if request.method == 'POST':
            datas = MyAirportCity(request.POST, instance=data)
            if datas.is_valid():
                datas.save()
                return redirect(reverse('cityManage', args=[aid.id]))
            # obj = datas.save(commit=False)
            # obj.fromCity = aid
            # obj.save()
            else:
                messages.error("Sorry, Something Went Wrong, Check Your Inputs...")
        else:
            messages.erroe("I think you sent a bad request, for security issues we cannot allow your submit")
        

        context = {
            'form': form
        }

        return render(request, 'admin/editCity.html', context)
    else:
        return render(request, 'admin/notAuthorised.html')

# Function to Delete the City

def deleteCity(request, pk):
    if request.user.is_superuser:
        data = airportCity.objects.get(id = pk)
        aid = airportRates.objects.get(id = data.fromCity.id)

        data.delete()
        return redirect(reverse('cityManage', args=[aid.id]))
    else:
        return render(request, 'admin/notAuthorised.html')


# Function to Delete the Airport

def deleteAirport(request, pk):
    if request.user.is_superuser:
        data = airportRates.objects.get(id = pk)
        data.delete()
        return redirect('addAirports')
    else:
        return render(request, 'admin/notAuthorised.html')


#To Fecth All Business Forms

def businessForms(request):
    if request.user.is_superuser:
        data = businessForm.objects.all()

        context = {
            'data': data
        }
        return render(request, 'admin/businessForms.html', context)
    else:
        return render(request, 'admin/notAuthorised.html')


#To Fetch Single Business Form
def businessFormView(request, pk):
    if request.user.is_superuser:
        data = businessForm.objects.get(id = pk)

        context = {
            'data':data
        }
        return render(request, 'admin/businessFormView.html', context)
    else:
        return render(request, 'admin/notAuthorised.html')