from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
def index(request):
    facilities = Facility.objects.all().order_by('id')
    cities = City.objects.all()
    states = State.objects.all()
    cityid = request.GET.get('city')
    print(cityid)
    hospitals = None
    if cityid:
        hospitals = Hospital.get_hospitals(cityid)
    else:
        hospitals = Hospital.objects.all()    
    avalabilities = Availability.objects.all()
    context={
        'facilities':facilities,
        'cities':cities,
        'states':states,
        'hospitals':hospitals,
        'avalability':avalabilities
    }
    return render(request,"index.html",context=context)

def see(request,hospital_id):
    hospitals = Hospital.objects.filter(id=hospital_id)
    context={
        'hospitals':hospitals
    }
    return render(request,"see.html",context)   