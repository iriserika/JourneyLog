from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render
from footprint.models import Location

# Create your views here.
def show_footprint(request):

    return render(request, 'footprint.html', {'locations': read_locations(request.user)})

def read_locations(user):
    locations = Location.objects.filter(author=user)
    loca_list = []
    for location in locations:
        loca_list.append([location.latitude, location.longitude])
    return loca_list

def add_location(request):

    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        # save the new location into db
        location = Location()
        location.author = request.user
        location.latitude = latitude
        location.longitude = longitude
        location.save()

    return render(request, 'footprint.html', {'locations': read_locations(request.user)})


