from django.shortcuts import render
from django.http import JsonResponse
from .models import ComplaintForm
import dashboard.models
from .forms import MyBusinessForm
from django.contrib import messages


# Create your views here.


#Function to Home Page

def home(request):
    data = dashboard.models.airportRates.objects.all()
    # other = ''
    # if request.method == 'POST':
    #     userName = request.POST['userName']
    #     dateOfJourney = request.POST['dateOfJourney']
    #     phoneNumber = request.POST['phoneNumber']
    #     pickUpAddress = request.POST['pickUpAddress']
    #     dropAddress = request.POST['dropAddress']
    #     complaintRegarding = request.POST['complaintRegarding']
    #     if request.POST['other']:
    #         other = request.POST['other']
    #         complaintRegarding = complaintRegarding + '-----' + other
    #     description = request.POST['description']

    #     form = ComplaintForm(userName = userName, 
    #                          dateOfJourney = dateOfJourney, 
    #                          phoneNumber = phoneNumber,
    #                          pickUpAddress = pickUpAddress,
    #                          dropAddress = dropAddress,
    #                          complaintRegarding = complaintRegarding,
    #                          description = description
    #                          )
        
    #     try: 
    #         form.save()
    #     except:
    #         print("Something Went Wrong.....") 
    # else:
    #     print("Something Went Wrong Here also......")
    return render(request, 'user/index.html', {'data':data})


#Function to Privacy Policy

def privacyAndPolicy(request):
    return render(request, 'user/privacy&policy.html')


#Function to Business Terms and Conditions

def businessTerms(request):
    return render(request, 'user/BusinessT&C.html')


#Function to Corporate

def corporate(request):
    return render(request, 'user/corporate.html')


#Function to Rides Page

def rides(request):
    return render(request, 'user/rides.html')


#Function to Driver Registration

def driverRegister(request):
    return render(request, 'user/DriverLogin.html')


#Function to Website Terms

def websiteTerms(request):
    return render(request, 'user/websiteTerms.html')



# Fuction to Get Complaint from user and store it in the Database

def complaintForm(request):
    other = ''
    if request.method == 'POST':
        userName = request.POST['userName']
        dateOfJourney = request.POST['dateOfJourney']
        phoneNumber = request.POST['phoneNumber']
        pickUpAddress = request.POST['pickUpAddress']
        dropAddress = request.POST['dropAddress']
        complaintRegarding = request.POST['complaintRegarding']
        if request.POST['other']:
            other = request.POST['other']
            complaintRegarding = complaintRegarding + '-----' + other
        description = request.POST['description']

        form = ComplaintForm(userName = userName, 
                             dateOfJourney = dateOfJourney, 
                             phoneNumber = phoneNumber,
                             pickUpAddress = pickUpAddress,
                             dropAddress = dropAddress,
                             complaintRegarding = complaintRegarding,
                             description = description
                             )
        
        try: 
            form.save()
            return render(request, 'user/complaintsuccess.html')
        except:
            print("Something Went Wrong.....")
    else:
        print("Something Went Wrong Here also......")
    
        



# Function to get the Business Details from the Client

def businessForm(request):
    # form = MyBusinessForm()
    # if request.method == 'POST':
    #     data = MyBusinessForm(request.POST)
    #     if data.is_valid():
    #         data.save()
    #     # else:
    #         # print("Something Went Wrong...")
    if request.method == "POST":
        companyName = request.POST['companyName']
        natureOfBusiness = request.POST['natureOfBusiness']
        WebsiteAddress = request.POST['WebsiteAddress']
        YearCompanyWasEstablished = request.POST['YearCompanyWasEstablished']
        contactName = request.POST['contactName']
        jobTitle = request.POST['jobTitle']
        department = request.POST['department']
        telephoneNumber = request.POST['telephoneNumber']
        emailAddress = request.POST['emailAddress']
        monthlyCreditAmount = request.POST['monthlyCreditAmount']
        monthlySpend = request.POST['monthlySpend']
        authorisedBy = request.POST['authorisedBy']

        form = dashboard.models.businessForm(Company_Name = companyName, Nature_Of_Business = natureOfBusiness, Website_Address = WebsiteAddress, Year_Company_Est = YearCompanyWasEstablished,contactName = contactName, Job_Title = jobTitle,
                                             Department = department,
                                             TelePhone_Number = telephoneNumber,
                                             Email_Address = emailAddress,
                                             Monthly_Credit_Amount = monthlyCreditAmount,
                                             Monthly_Spend = monthlySpend,
                                             Authorised_By = authorisedBy,
                                             Terms_And_Conditions = True)
        
        try:
            form.save()
            messages.error(request, 'Something Went Wrong')
        except:
            return messages.error(request, 'Check Your Inputs..')
    
    return render(request, 'user/corporate.html')


#Function to Get the Destination from the Selected Airport

def airportDest(request):
    if request.method == 'GET':
        fromCity = request.GET['dest']
        dest = dashboard.models.airportCity.objects.filter(fromCity = dashboard.models.airportRates.objects.get(id = fromCity))
        dest_list = list(dest.values())
        return JsonResponse({'dest': dest_list})