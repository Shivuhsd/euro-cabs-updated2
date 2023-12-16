from django.shortcuts import render, redirect
from django.urls import reverse
import users.models
from . models import airportRates, airportCity, businessForm
from django.http import HttpResponse, JsonResponse
from .forms import MyAirportCity

# Create your views here.

# Fuction to Load Dashboard of the Admin

def adminDashborad(request):
    
    return render(request, 'admin/dashboard.html')

# Function to Load the Complaints to the user

def complaints(request):
    if request.user.is_superuser:
        data = users.models.ComplaintForm.objects.all()

        context = {
            'complaints': data
        }
    else:
        return HttpResponse("You Are Not Authorized....")
    return render(request, 'admin/complaints.html', context)


# Function to Display the Complaint to Admin

def showComplaint(request, pk):
    try:
        data = users.models.ComplaintForm.objects.get(id = pk)

        context = {
            'data': data
        }
        return render(request, 'admin/showComplaint.html', context)
    except:
        return custom404(request)

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


# Function to Manage the City

def cityManage(request, pk):
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
            print("Some Thing is Wrong in your data")
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


# Custom View for 404(Page Not Found)

def custom404(request, exception = None):
    return render(request, 'admin/404.html', status=404)



# Function to Edit the City

def editCity(request, pk):
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
            pass
    else:
        pass

    context = {
        'form': form
    }

    return render(request, 'admin/editCity.html', context)

# Function to Delete the City

def deleteCity(request, pk):
    data = airportCity.objects.get(id = pk)
    aid = airportRates.objects.get(id = data.fromCity.id)

    data.delete()
    return redirect(reverse('cityManage', args=[aid.id]))


# Function to Delete the Airport

def deleteAirport(request, pk):
    data = airportRates.objects.get(id = pk)
    data.delete()
    return redirect('addAirports')


#To Fecth All Business Forms

def businessForms(request):
    data = businessForm.objects.all()

    context = {
        'data': data
    }
    return render(request, 'admin/businessForms.html', context)


#To Fetch Single Business Form
def businessFormView(request, pk):
    data = businessForm.objects.get(id = pk)

    context = {
        'data':data
    }
    return render(request, 'admin/businessFormView.html', context)