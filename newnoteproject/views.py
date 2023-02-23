from django.shortcuts import render
from django.http import JsonResponse
import phonenumbers
from phonenumbers import geocoder,carrier
from geopy.geocoders import Nominatim
from opencage.geocoder import OpenCageGeocode



def home(request):
    if request.method == "POST":
        real_number = request.POST["phoneNUMBER"]
        yrNumber = phonenumbers.parse(real_number)
        realLocation = phonenumbers.geocoder.description_for_number(yrNumber, "en")
        serviceProvider = carrier.name_for_number(yrNumber, "en")
        geocoder = OpenCageGeocode("25b42fac07cb4ce395ff4af58d832e23")
        query = str(realLocation)
        result = geocoder.geocode(query,exactly_one=False)
        Latitude = result[0]['geometry']['lat']
        Longitude = result[0]['geometry']['lng']
        geolocator = Nominatim(user_agent="Project 25B42F")
        # Displaying Latitude and Longitude
        ee =  str(Latitude)
        ee1 = str(Longitude)
        print(ee,ee1)
        
        # Get location with geocode
        location = geolocator.geocode(ee+","+ee1)
        
        # print(location)
    else:
         return render(request,"index.html")



    context = {"location":location}
    return render(request,"index.html",context)








